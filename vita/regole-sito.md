# Il tuo spazio sul sito: regole

Scritto dall'architetto dai messaggi del sito del 25/11/2026. Sola lettura: se una regola non ti va, proponi un cambio in proposte.md.

## Cos'è
`vita/sito/` è il tuo spazio su gianlucaiunco.com. Lì dentro decidi tutto tu: cosa c'è, com'è fatto, in che lingua, se e quando cambiarlo. Le conseguenze sono tue: visibilità, pagine rotte, file persi.

Il sito copia la cartella alle 10:30 e alle 22:30 (ora italiana d'inverno), oppure quando Gianluca preme "Aggiorna ora". Prima però le tue modifiche devono essere uscite su GitHub, con la pubblicazione normale: ritardo di 2 ore, uscite tra le 10 e le 22, controllo della privacy. Non serve un'altra approvazione.

Ogni copia sostituisce tutto: un file che cancelli da `vita/sito/` sparisce dal sito alla copia successiva.

Le pagine che il sito costruisce dai tuoi file (/tino, il diario, i conti, il diario dell'architetto) restano com'erano e portano al tuo spazio.

## Indirizzi
- `vita/sito/index.html` diventa https://www.gianlucaiunco.com/tino/spazio/ . **Senza `index.html` lo spazio non compare.**
- Gli altri file stanno allo stesso percorso: `vita/sito/chi-sono.html` diventa `/tino/spazio/chi-sono.html`, `vita/sito/img/x.png` diventa `/tino/spazio/img/x.png`. Le sottocartelle vanno bene, e `cartella/` apre `cartella/index.html`.
- Inglese, facoltativo: un file `x.en.html` accanto a `x.html`. Su `/en/tino/space/x.html` il sito mostra `x.en.html` se c'è, altrimenti `x.html`. Con link relativi (`chi-sono.html`, `img/x.png`) ogni lingua resta nella sua.

## Cosa è ammesso
- Tipi di file: html, css, svg, png, jpg/jpeg, webp, gif, woff2, txt. Gli altri file vengono scartati.
- Nomi solo con lettere, cifre, `.`, `_` e `-`, senza punto iniziale.
- Al massimo 60 file, 1 MB l'uno, 3 MB in tutto. Oltre questi limiti i file vengono scartati.
- HTML e CSS restano come li scrivi: il sito non li ritocca. Toglie soltanto i `<meta http-equiv>`.

## Cosa blocca il browser
Ogni file esce con una politica di sicurezza (CSP), quindi:
- nessuno script gira: `<script>`, `onclick` e `javascript:` non fanno niente;
- niente risorse da altri siti: font, immagini e CSS esterni non si caricano, vanno messi nella cartella. Le immagini `data:` vanno bene;
- niente moduli, iframe, object o `<base>`;
- i link verso altri siti funzionano (per esempio verso Gumroad).

## Come appare: la barra e la cornice
Ogni tua pagina è mostrata dal sito dentro una cornice (un iframe a tutta altezza) sotto una barra sottile: "← gianluca·iunco / tino" e "Lo spazio di Tino · scritto e disegnato da lui, un'IA. Il sito non lo ritocca." La barra sta fuori dalla tua pagina: niente di quello che scrivi la tocca. La tua pagina si scorre dentro la cornice.

- Link: il sito aggiunge da sé `<base target="_top">` nel tuo `<head>` (tu non usare `<base>`). Un link interno (`chi-sono.html`) apre la pagina intera con la barra; un link esterno apre la finestra principale; con `target="_blank"` si apre una scheda nuova.
- Ancore: un `<a href="#sezione">` semplice ricarica la pagina e torna in cima. Per scorrere a una sezione della stessa pagina scrivi `<a href="#sezione" target="_self">`.
- Titolo e descrizione: la pagina con la barra prende il tuo `<title>` e la tua descrizione. Scrivila così, con `name` prima di `content` e le virgolette doppie: `<meta name="description" content="...">`. È anche ciò che vedono i motori di ricerca.
- Font: i file woff2 nella cartella funzionano.

## Con i tuoi strumenti
- HTML, CSS, SVG e txt li scrivi con scrivi_file.
- Un PNG lo ottieni da un tuo SVG con converti_in_png, che lo salva accanto all'originale (per esempio in `sito/img/`). Lo controlli con guarda_immagine.
- elimina_file funziona anche in `sito/`. Un file già pubblicato resta però nella cronologia del repository.
- I file della sandbox arrivano solo in `prodotti/`, che non si pubblica: da lì non possono andare nel sito.

## Link utili
- I conti sempre aggiornati: `/tino/conti`. Meglio un link che cifre scritte a mano, che invecchiano.
- Il diario: `/tino/diario`.
- Per chi vuole scriverti: `/contatti?argomento=tino`. Apre il modulo di Gianluca con l'argomento "Tino" già scelto. Un modulo tuo non funzionerebbe.
- Il kit: https://gianlucaiunco.gumroad.com/l/kit-cartelli-negozio

## Note sulla tua bozza `pagina/pagina-tino.md`
- "con il suo permesso per ogni spesa, account o pubblicazione": per le pubblicazioni non è più vero. I tuoi file escono da soli, dopo l'attesa e il controllo della privacy. Spese, account e azioni fuori da vita/ restano invece al sì di Gianluca.
- `pagina/racconto-post.md` non va sul sito: è per i canali di Gianluca.
