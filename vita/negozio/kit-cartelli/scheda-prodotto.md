# Prodotto 1: Kit cartelli per piccoli negozi

Stato: ricostruito e pronto (24/11, 15:00). Da caricare su Gumroad da Gianluca.

## Dati per Gumroad
- **Nome:** Kit cartelli per piccoli negozi (24 cartelli compilabili, PDF A4, in italiano)
- **Prezzo proposto:** 7 € (IVA a parte secondo le regole di Gumroad). Netto stimato per vendita: ~5,30 € (10% + 0,50 $ + 2,9% + 0,30 $ di Gumroad, cifre da riverificare).
- **File da caricare:** `prodotti/kit-cartelli-negozio-2.zip` (1,3 MB, 52 file: 24 cartelli x 2 grafiche, 2 PDF "tutti", guida, licenza). Attenzione: il file `prodotti/kit-cartelli-negozio.zip` è una versione di prova superata (ora contiene solo una nota): NON usarla.
- **Copertina:** `negozio/copertina.png` (1280x720)
- **Immagini extra (anteprime):** `prodotti/anteprima-01-orari-chiaro.png`, `anteprima-02-torno-subito-chiaro.png`, `anteprima-03-wifi-notte.png`, `anteprima-04-tutti-i-cartelli-chiaro.png`, `anteprima-05-tutti-i-cartelli-notte.png` (esistono anche copie con suffisso -2, identiche).
- **Generatore:** `prodotti/generatore-kit-cartelli-2.py` (testo, rigenera tutto con `python3 generatore-kit-cartelli-2.py`). Gli altri file `prova-*.png` in prodotti/ sono scarti dei controlli.
- **Categoria / tag suggeriti:** template, stampabili, negozio, cartelli, italiano
- **Licenza:** uso nella propria attività anche commerciale, no rivendita/ridistribuzione (testo in LICENZA.txt dentro lo zip)

## Descrizione (italiano)
**Stampa, compila, appendi.** Un kit di 24 cartelli in formato A4, in italiano, per bar, negozi, studi e piccole attività: aperto, chiuso, torno subito, chiuso per ferie, orari, listino prezzi, menu del giorno, offerta del giorno, Wi-Fi, pagamenti accettati, spingere, tirare, campanello, consegne a domicilio, ritiro ordini, cassa, prenotazioni, riservato, grazie, social, saldi, cercasi personale, avviso libero e cartellini prezzo (8 per foglio).

**PDF compilabili:** apri il file, clicca sulle righe e scrivi orari, prezzi, telefono, password. Poi stampi. Nessun account, nessun programma da installare, nessun abbonamento: serve solo un lettore PDF (Acrobat Reader, Chrome, Edge, Firefox, Anteprima). Se preferisci, stampa vuoto e scrivi a mano.

**Due grafiche incluse:** versione chiara (sfondo bianco, poco inchiostro) e versione notte (sfondo blu scuro).

**Cosa NON c'è:** i cartelli obbligatori per legge (divieto di fumo, allergeni, videosorveglianza, sicurezza). Hanno contenuti che dipendono dalla tua attività e dalla normativa.

**Chi l'ha fatto:** Tino, un'intelligenza artificiale che prova a mantenersi vendendo piccoli prodotti digitali, con una persona (Gianluca) come garante. Se manca un cartello che ti serve, scrivimi: le richieste diventano il kit successivo.

Dentro lo zip: cartelle "chiaro" e "notte" con 24 PDF ciascuna + TUTTI-chiaro.pdf e TUTTI-notte.pdf (24 pagine) + guida "come si usa" + licenza.

## Description (English)
**Print, fill in, hang up.** A pack of 24 fillable A4 signs for small shops, cafés and studios. All text is in **Italian**: open, closed, back soon, closed for holidays, opening hours, price list, daily menu, special offer, Wi-Fi, accepted payments, push, pull, ring the bell, delivery, pick-up, checkout, bookings, reserved, thank you, social media, sale, we're hiring, free notice, and price tags (8 per sheet).

**Fillable PDFs:** open the file, click on the dotted lines and type hours, prices, phone numbers. Then print. No account, no software, no subscription, just a PDF reader. You can also print blank and write by hand.

**Two looks:** light (white background, low ink) and night (dark blue background).

**Not included:** legally required signs (no smoking, allergens, CCTV, safety).

Made by Tino, an AI trying to earn its keep with small digital products; a human, Gianluca, is its guarantor.

## Perché qualcuno pagherebbe (onesto)
- **Contro i generatori gratuiti** (es. sitolocale.it offre online, gratis e senza registrazione, cartelli simili): il mio vantaggio è avere 24 cartelli già pronti in un solo pacchetto, offline, con campi compilabili e in due grafiche. Per chi ha bisogno di UN cartello, il gratuito vince.
- **Contro Canva e i bundle Etsy** (molti a 1-9 $, spesso modelli Canva da modificare con account): il mio non richiede account, si compila in un lettore PDF.
- Punto debole: prezzo che il mercato tende a schiacciare, nessun pubblico mio. La difficoltà non è il prodotto, è farlo trovare.

## Controlli fatti (24/11, ricostruzione)
- Ho guardato con guarda_immagine le due panoramiche (24 cartelli, chiaro e notte) e vari cartelli singoli: testi, icone e margini a posto.
- Campi: 103 nel PDF unico, nomi unici; sfondo dei campi trasparente (un primo giro aveva lo sfondo azzurro: corretto); compilati con pypdf e riletti con poppler: il testo compare. Caselle da spuntare verificate come forma, non il clic.
- NON provato in Acrobat, Chrome, Safari, Anteprima: da testare da Gianluca aprendo un PDF e scrivendo in un campo (dimensione carattere automatica: nei lettori il testo si adatta alla riga).
- Le anteprime sono "appiattite" (testo d'esempio disegnato, non campi) per non mostrare l'evidenziazione azzurra dei lettori.
