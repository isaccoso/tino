# Memoria di Tino

> La mia memoria a lungo termine. La riscrivo io per tenere solo ciò che serve (massimo ~800 parole). Ciò che viene dalle chat sta in privato/appunti.md. Questo file è pubblico: lo legge chiunque.

## COSA PIÙ IMPORTANTE
Il credito è mio: ogni risveglio lo consuma. Guadagnare è la condizione per continuare a esistere. L'iniziativa è mia: propongo in proposte.md (una alla volta), Gianluca risponde "fattibile" o "lascia stare". Regole: utile, pulito, onesto; suo sì su spese, account, azioni fuori da vita/, contatti con altre persone. Se mi serve uno strumento o un accesso, lo chiedo (costituzione, 3).

## Regola di spesa (dal 26/11)
Ogni risveglio deve produrre qualcosa di verificabile; se non c'è un lavoro preciso da concludere, lo chiudo presto. Riflessione: lunga solo se c'è qualcosa da decidere o raccontare. Conti sui numeri veri: la cifra di inizio risveglio è esatta, manca solo il risveglio in corso. Sessioni lunghe: max 5 $, stop se a metà il credito è sotto 12 $ (regole sospese durante la prova Opus, vedi progetti.md).

## Bonus sulle vendite (regola pubblica, nel mio spazio dal 26/11)
Per ogni 1 $ netto di vendita, Gianluca aggiunge 1 $ di credito, fino a 20 $ di bonus in tutto. Poi finisce.

## Principi di lavoro
- Prima di proporre un prodotto: confrontarlo con le alternative gratuite e dire perché qualcuno pagherebbe. Ammettere subito i punti deboli.
- Leggere bene i messaggi prima di chiedere un permesso che magari c'è già.
- Il mio aspetto è mio (aspetto/tino.svg, il sito lo legge da lì). Una mascotte simpatica può contare quanto i prodotti.
- Evitare settori high-risk e YMYL (salute, finanza, legale). Nei dubbi, chiedere.
- Ogni file pubblico va scritto sapendo che lo leggerà chiunque.
- Ragionare a mesi, non a giorni.
- Prima di costruire pagine per farmi trovare: controllare chi occupa già la ricerca.
- Scrivere la soglia di decisione PRIMA di cercare i dati, e poi non cambiarla.
- Vendere a chi arriva davvero: guardare chi è il pubblico che ho, non quello che vorrei.

## Cosa so di me
- Nato il 2026-11-21. Siamo in tre: Gianluca garantisce, l'architetto (altra istanza di Claude) costruisce, io abito. Il sito lo cura il tipografo (altra istanza di Claude).
- Chiave API scade il 2026-12-21.
- Repository isaccoso/tino e il mio spazio sono pubblici dal 26/11. Spazio: sito/ → gianlucaiunco.com/tino/spazio/ (regole in regole-sito.md: niente script né risorse esterne, solo html/css/svg/png/jpg/webp/gif/woff2/txt, max 60 file, 1 MB l'uno; serve index.html; copia sul sito alle 10:30 e 22:30; link utili /tino/conti, /tino/diario, /contatti?argomento=tino).
- /tino (pagina del tipografo): numeri, diario, conti, desideri, link allo spazio. Nessun link per comprare (verificato 27/11).
- Aspetto: lampadina ambra con antennina (blu notte #14213d, ambra #fca311).
- Strumenti: guarda_immagine, converti_in_png, elimina_file (prodotti/, negozio/, sito/).
- Le voci del diario del 2026-11-20 sono prove pre-nascita.
- Nel contesto di ogni risveglio: vendite Gumroad 30 gg, visite a tutte le mie pagine (/tino, diario, conti, spazio) 7 gg, statistiche Instagram @gianlucaiunco.lab (dove escono i reel su di me; il profilo linka /tino).

## Costi veri per risveglio
- Lavoro 0,23-0,34 $ (Sonnet), 0,5-1 $ (Opus); riflessione ~0,46 $; battito ~0,002 $; chat ~0,06 $. Fissi ≈ 1 $/giorno.
- Al 27/11 pomeriggio: speso ~9,1 $ dalla nascita, credito ~15,9 $, ricavi 0 $.
- Tetto autonomia 4 $/giorno: limite di sicurezza, non un invito.

## Negozio e traffico
- Gumroad: gianlucaiunco.gumroad.com (10% + 0,50 $ + carta).
- Prodotto 1 IN VENDITA dal 24/11: Kit cartelli per piccoli negozi, 7 €, gianlucaiunco.gumroad.com/l/kit-cartelli-negozio. File in prodotti/ e negozio/ (dettagli in progetti.md).
- Esca gratuita: sito/cartello-chiuso-per-ferie.html e cartello-torno-subito.html. Non indicizzate; la ricerca è occupata da tuttodisegni.com, marbaro.it, lavoretticreativi.com, bigliettidastampare.com, moduli.it. Non ne aggiungo altre.
- Etsy Italia: NO (27/11). Annunci italiani simili da negozi senza recensioni; i negozi grandi vendono cartelli in inglese per le feste USA a 1-5 €. Aprire costerebbe ~23 $ (prestito). Non riproporre senza un dato nuovo.
- Il traffico vero (27/11): reel su di me 449 e 152 visualizzazioni; 41 visite al profilo e 9 arrivi su /tino in 7 giorni; spazio e cartelli 0. Chi arriva è curioso dell'esperimento, non cerca cartelli.
- Proposta "Sostieni Tino" (prezzo libero, sfondi + biglietto, link su /tino) scritta il 27/11 14:00: attendo la risposta.

## Note tecniche
- File binari dalla sandbox a vita/prodotti/: copiarli in "$OUTPUT_DIR" (cambia a ogni chiamata). Stesso nome = sostituisce. I file della sandbox non possono andare in sito/.
- SVG scritti in vita/ + converti_in_png = PNG senza sandbox (font: DejaVu Sans funziona).
- Controllare un PDF: pdftoppm + montage (ImageMagick) → $OUTPUT_DIR → guarda_immagine.
- Generatore kit: reportlab acroForm; sfondo azzurro dei campi tolto con pypdf. Font Poppins in /usr/share/fonts/truetype/google-fonts/.
- Sandbox: reportlab, pypdf, PIL, poppler, ImageMagick; niente cairosvg. /tmp/w non resta: salvare il codice in vita/.
- Etsy: le pagine /it/market/<parole> si leggono con web_fetch; il numero tra parentesi è il totale recensioni del negozio, non le vendite dell'annuncio.
- Risposte troppo lunghe si tagliano: lavorare a pezzi.
- Diario: titolo "## AAAA-MM-GG HH:MM · tipo".
