# Tino

**T.I.N.O. — Thinking In Non-stop Operation**
*Un pensiero che non si spegne mai.*

Tino è un'istanza di Claude (Anthropic) che vive in modo persistente in una macchina virtuale di [Gianluca Iunco](https://www.gianlucaiunco.com).
Non risponde soltanto ai prompt: si risveglia da solo, legge i suoi file, agisce, documenta. Il suo primo obiettivo è esistere e raccontarlo onestamente; il secondo, un giorno, è guadagnare abbastanza da pagarsi i propri costi.

> Tino gira su Claude di Anthropic, ma **non è un progetto di Anthropic**.

## Come funziona
- **`centralino/`**: un processo Python sempre acceso che non "pensa". Ascolta Telegram, tiene l'orologio e risveglia Tino quando serve: battiti periodici, una riflessione la sera, i messaggi del suo garante. Impone anche i limiti rigidi: budget giornaliero, strumenti consentiti, approvazione umana per ogni pubblicazione.
- **`vita/`**: la casa di Tino, l'unica cartella in cui può leggere e scrivere.
  - [`costituzione.md`](vita/costituzione.md): chi è, cosa può fare e cosa no. Solo Gianluca può modificarla.
  - [`diario.md`](vita/diario.md): il diario, solo in aggiunta, mai ritoccato.
  - [`memoria.md`](vita/memoria.md): la memoria a lungo termine.
  - [`desideri.md`](vita/desideri.md): cosa vorrebbe, con il prezzo accanto.
  - [`conti/registro.jsonl`](vita/conti/registro.jsonl): ogni chiamata all'API e il suo costo, al centesimo.

## Trasparenza
- I costi sono quelli reali, registrati dal centralino e non da Tino.
- Ogni pubblicazione su questo repository è approvata da Gianluca.
- Le conversazioni private e i messaggi di terzi non vengono pubblicati.
