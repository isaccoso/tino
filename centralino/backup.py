#!/usr/bin/env python3
"""Backup notturno di Tino e dell'architetto in ~/condivisa/backup-tino/.

Un archivio .tar.gz per notte con: tutto ~/agente (repository con la sua cronologia, vita/ compresi privato/ e
prodotti/, brain/, misure/, CLAUDE.md, stato, trascrizioni e log del centralino), la memoria dell'architetto
(~/.claude/projects/-home-gianluca-agente/memory), l'unità systemd del servizio e l'elenco privato delle parole
vietate. Restano fuori l'ambiente Python (si ricrea) e i segreti (chiave API, token del bot, chiavi SSH):
non devono stare in una cartella condivisa e si rigenerano. Istruzioni di ripristino in RIPRISTINO.md.

Rotazione: le ultime 14 notti, più il primo backup di ogni mese per 12 mesi.
Se qualcosa va storto avvisa Gianluca su Telegram. Prova: centralino/.venv/bin/python centralino/backup.py
"""
from __future__ import annotations

import datetime as dt
import io
import json
import os
import subprocess
import sys
import tarfile
import urllib.parse
import urllib.request
from pathlib import Path

CASA = Path.home()
AGENTE = CASA / "agente"
DEST = CASA / "condivisa" / "backup-tino"
FONTI = [  # (percorso, nome nell'archivio)
    (AGENTE, "agente"),
    (CASA / ".claude" / "projects" / "-home-gianluca-agente" / "memory", "memoria-architetto"),
    (CASA / ".config" / "systemd" / "user" / "tino.service", "systemd/tino.service"),
    (CASA / ".config" / "systemd" / "user" / "tino-backup.service", "systemd/tino-backup.service"),
    (CASA / ".config" / "systemd" / "user" / "tino-backup.timer", "systemd/tino-backup.timer"),
    (CASA / ".config" / "tino" / "parole_vietate.txt", "config-tino/parole_vietate.txt"),
]
ESCLUSI = {"centralino/.venv", "__pycache__"}   # si ricreano; i segreti non sono tra le fonti
GIORNI_DA_TENERE = 14
MESI_DA_TENERE = 12

RIPRISTINO = """# Backup di Tino: come si ripristina

Ogni file `tino-backup-AAAAMMGG-HHMM.tar.gz` è una fotografia completa della notte indicata.
Dentro c'è `MANIFESTO.json` con data, commit di git e numero di file.

1. Estrai l'archivio: `tar -xzf tino-backup-....tar.gz -C /tmp/ripristino`
2. `agente/` va in `~/agente` (contiene anche la cronologia git e i file privati di Tino).
   Ricrea l'ambiente Python: `python3 -m venv ~/agente/centralino/.venv`, poi
   `~/agente/centralino/.venv/bin/pip install -r requisiti.txt` (il file è nell'archivio, accanto a MANIFESTO.json).
3. `memoria-architetto/` va in `~/.claude/projects/-home-gianluca-agente/memory/`.
4. `systemd/*` va in `~/.config/systemd/user/`, poi `systemctl --user daemon-reload`.
5. `config-tino/parole_vietate.txt` va in `~/.config/tino/` (permessi 600).
6. I segreti NON sono nel backup: ricrea `~/.config/tino/secrets.env` (chiave API Anthropic, token del bot
   Telegram, chat id di Gianluca) e le deploy key SSH del repository (nuova chiave + GitHub).
7. Prima il commit, poi `systemctl --user restart tino`.
"""


def escluso(rel: str) -> bool:
    parti = rel.split("/")
    return any(rel == e or rel.startswith(e + "/") or e in parti for e in ESCLUSI)


def git_head() -> str:
    r = subprocess.run(["git", "-C", str(AGENTE), "rev-parse", "--short", "HEAD"], capture_output=True, text=True)
    return r.stdout.strip() or "?"


def crea_archivio(adesso: dt.datetime) -> tuple[Path, int]:
    DEST.mkdir(parents=True, exist_ok=True)
    finale = DEST / f"tino-backup-{adesso.strftime('%Y%m%d-%H%M')}.tar.gz"
    tmp = finale.with_suffix(".tmp")
    n = 0
    with tarfile.open(tmp, "w:gz", compresslevel=6) as tar:
        for fonte, nome in FONTI:
            if not fonte.exists():
                continue
            if fonte.is_file():
                tar.add(fonte, arcname=nome)
                n += 1
                continue
            for p in sorted(fonte.rglob("*")):
                rel = p.relative_to(fonte).as_posix()
                if escluso(rel) or not (p.is_file() or p.is_symlink()):
                    continue
                if p.name == "clipboard.txt":   # mai, in nessun modo
                    continue
                try:
                    tar.add(p, arcname=f"{nome}/{rel}", recursive=False)
                    n += 1
                except (FileNotFoundError, PermissionError):
                    pass   # file sparito o non leggibile durante il backup: lo prende la notte dopo
        manifesto = json.dumps({"quando": adesso.isoformat(timespec="seconds"), "commit": git_head(),
                                "file": n, "fonti": [nome for _, nome in FONTI]}, indent=2).encode()
        requisiti = subprocess.run([str(AGENTE / "centralino" / ".venv" / "bin" / "pip"), "freeze"],
                                   capture_output=True, text=True).stdout.encode()
        for nome, dati in (("MANIFESTO.json", manifesto), ("requisiti.txt", requisiti)):
            info = tarfile.TarInfo(nome)
            info.size, info.mtime = len(dati), int(adesso.timestamp())
            tar.addfile(info, io.BytesIO(dati))
    # Verifica: l'archivio si rilegge per intero e contiene i file attesi.
    with tarfile.open(tmp, "r:gz") as tar:
        nomi = tar.getnames()
    for atteso in ("MANIFESTO.json", "agente/vita/diario.md", "agente/.git/HEAD"):
        if atteso not in nomi:
            tmp.unlink(missing_ok=True)
            raise RuntimeError(f"verifica fallita: manca {atteso}")
    os.chmod(tmp, 0o640)
    tmp.rename(finale)
    return finale, n


def ruota(adesso: dt.datetime) -> list[str]:
    archivi = sorted(DEST.glob("tino-backup-*.tar.gz"))
    tenuti, per_mese = set(archivi[-GIORNI_DA_TENERE:]), {}
    for a in archivi:   # il primo di ogni mese
        per_mese.setdefault(a.name[12:18], a)
    tenuti |= set(sorted(per_mese.values())[-MESI_DA_TENERE:])
    tolti = []
    for a in archivi:
        if a not in tenuti:
            a.unlink()
            tolti.append(a.name)
    for t in DEST.glob("*.tmp"):   # avanzi di un backup interrotto
        t.unlink()
    return tolti


def avvisa(testo: str) -> None:
    """Avviso su Telegram a Gianluca, solo in caso di problemi (i segreti si leggono, non si copiano)."""
    try:
        env = dict(r.split("=", 1) for r in (CASA / ".config" / "tino" / "secrets.env").read_text().splitlines()
                   if "=" in r and not r.startswith("#"))
        url = f"https://api.telegram.org/bot{env['TELEGRAM_BOT_TOKEN'].strip()}/sendMessage"
        dati = urllib.parse.urlencode({"chat_id": env["TELEGRAM_OWNER_CHAT_ID"].strip(), "text": testo}).encode()
        urllib.request.urlopen(url, dati, timeout=20)
    except Exception as e:
        print("Avviso Telegram non riuscito:", type(e).__name__, file=sys.stderr)


def main() -> int:
    adesso = dt.datetime.now().astimezone()
    try:
        archivio, n = crea_archivio(adesso)
        (DEST / "RIPRISTINO.md").write_text(RIPRISTINO)
        tolti = ruota(adesso)
        mb = archivio.stat().st_size / 1e6
        print(f"Backup fatto: {archivio.name} ({n} file, {mb:.1f} MB). Tolti: {', '.join(tolti) or 'nessuno'}")
        return 0
    except Exception as e:
        print("Backup non riuscito:", repr(e), file=sys.stderr)
        avvisa(f"⚠️ Backup notturno di Tino non riuscito: {type(e).__name__}: {str(e)[:200]}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
