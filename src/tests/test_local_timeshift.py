# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestLocalTimeshift(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_timeshift_sintonizzazione_su_un_canale_con_timeshift(self):
        # Tags: Timeshift
        # TODO: Implement action: "Sintonizzarsi su un canale che supporta il timeshift"
        # TODO: Implement result: "Il banner appare con l'icona di pausa visibile, il timing e la durata del programma. La posizione del cursore della progress bar dipende dall'avanzamento reale del programma. Le icone di seek non sono visibili."
        raise NotImplementedError

    def test_timeshift_sintonizzazione_su_un_canale_senza_timeshift(self):
        # Tags: Timeshift
        # TODO: Implement action: "Sintonizzarsi su un canale che non supporta il timeshift"
        # TODO: Implement result: "Il banner appare senza nessuna icona a sinistra della progress bar e icone di seek. La posizione del cursore della progress bar dipende dall'avanzamento reale del programma "
        raise NotImplementedError

    def test_timeshift_playpause_durante_il_live(self):
        # Tags: Timeshift
        # TODO: Implement action: "Stato: il canale su cui si è sintonizzati supporta il timeshift"
        # TODO: Implement action: "Premere il tasto play/pause sul telecomando durante il live "
        # TODO: Implement result: "Il banner appare se non è visibile."
        # TODO: Implement result: "A sinistra della progress bar scompare l'icona di pausa e compare quella di play."
        # TODO: Implement result: "Il timing e la durata del programma si azzerano (\"-00:00 00:00\")."
        # TODO: Implement result: "L'audio è silenziato."
        # TODO: Implement result: "Se si tratta della prima pausa, sotto la progress bar appaiono le icone di seek e il cursore si sposta all'inizio della progress bar.  "
        # TODO: Implement result: "A partire dalla seconda pausa il cursore si sposta verso sinistra sempre più lentamente. Il timing è decrementato di un secondo ogni secondo e corrisponde alla posizione corrente rispetto al live."
        raise NotImplementedError

    def test_timeshift_playpause_durante_la_pausa(self):
        # Tags: Timeshift
        # TODO: Implement action: "Premere il tasto play/pause durante la pausa"
        # TODO: Implement result: "Scompare l'icona di pause e compare quella di play. Il timing si blocca e il cursore si muove verso destra sempre più lentamente."
        raise NotImplementedError

    def test_timeshift_ffrewind_durante_il_live(self):
        # Tags: Timeshift
        # TODO: Implement action: "Premere il tasto FF/Rewind durante il live"
        # TODO: Implement result: "Se dall'ultima sintonizzazione non si è mai andati in pausa Fast Forward e Rewind sono disabilitati."
        # TODO: Implement result: "Se si è già andati almeno una volta in pausa il FF continua a non avere effetto. Premendo il tasto Rewind, la relativa icona compare a sinistra della progress bar, il cursore si muove verso sinistra più velocemente di quando si è in pausa e il timing è decrementato di più di un secondo al secondo. La durata del programma si azzera. Quando il cursore raggiunge l'inizio della progress bar si torna in stato di play"
        raise NotImplementedError

    def test_timeshift_ffrewind_durante_il_play_non_live(self):
        # Tags: Timeshift
        # TODO: Implement action: "Premere il tasto FF/Rewind durante lo stato di play (non live) "
        # TODO: Implement result: "Appare la relativa icona a sinistra della progress bar. Il timing è incrementato (decrementato) di più di un secondo al secondo e il cursore si sposta verso destra (sinistra). Se il cursore arriva all'inizio della progress bar si torna allo stato di play, se arriva alla fine si torna al live. "
        raise NotImplementedError

    def test_timeshift_ffrewind_durante_la_pausa(self):
        # Tags: Timeshift
        # TODO: Implement action: "Premere il tasto FF/Rewind durante lo stato di pause"
        # TODO: Implement result: "Appare la relativa icona a sinistra della progress bar. Il timing è incrementato (decrementato) di più di un secondo al secondo e il cursore si sposta verso destra (sinistra). Se il cursore arriva all'inizio della progress bar si torna allo stato di play, se arriva alla fine si torna al live. Quando viene interrotto il FF/Rewind c'è una transizione dallo stato di pause allo stato di play."
        raise NotImplementedError

    def test_timeshift_ff_durante_il_fast_forward(self):
        # Tags: Timeshift
        # TODO: Implement action: "Premere il tasto FF durante lo stato Fast Forward"
        # TODO: Implement result: "La velocità del playback aumenta di uno (2x->3x->4x->5x) fino a massimo 5x. "
        raise NotImplementedError

    def test_timeshift_rewind_durante_il_rewind(self):
        # Tags: Timeshift
        # TODO: Implement action: "Premere il tasto Rewind durante lo stato Rewind"
        # TODO: Implement result: "La velocità del playback aumenta di uno (-2x -> -3x -> -4x -> -5x) fino a massimo -5x. "
        raise NotImplementedError

    def test_timeshift_ff_durante_il_rewind(self):
        # Tags: Timeshift
        # TODO: Implement action: "Premere il tasto FF durante lo stato Rewind"
        # TODO: Implement result: "La velocità del playback si inverte di uno (2x->3x->4x->5x) fino a massimo 5x."
        raise NotImplementedError

    def test_timeshift_rewind_durante_il_fast_forward(self):
        # Tags: Timeshift
        # TODO: Implement action: "Premere il tasto Rewind durante lo stato Fast Forward"
        # TODO: Implement result: "La velocità del playback si inverte di uno (con direzione inversa rispetto al FF) fino a massimo -5x."
        raise NotImplementedError

    def test_timeshift_seek_next(self):
        # Tags: Timeshift
        # TODO: Implement action: "Premere il tasto seek (next) "
        # TODO: Implement result: "Dallo stato di Play, FF o Rewind il playback torna al live"
        # TODO: Implement result: "Dallo stato di pause il playback torna al live ma rimane in pausa."
        raise NotImplementedError

    def test_timeshift_seek_previous(self):
        # Tags: Timeshift
        # TODO: Implement action: "Premere il tasto seek (previous) "
        # TODO: Implement result: "Dallo stato di Play, FF o Rewind il playback torna all'inizio del buffer in stato di Play."
        # TODO: Implement result: "Dallo stato di Pause il playback torna all'inizio del buffer e rimane in pausa."
        raise NotImplementedError

    def test_timeshift_riempimento_del_buffer(self):
        # Tags: Timeshift
        # TODO: Implement action: "Rimanere in pausa fino al riempimento del buffer"
        # TODO: Implement result: "Appare il popup che avverte l'utente che il buffer è pieno e si torna allo stato di live "
        raise NotImplementedError

    def test_timeshift_ff_dopo_la_prima_pausa(self):
        # Tags: Timeshift
        # TODO: Implement action: "Sintonizzarsi su un canale andare in pausa. Aspettare 10 secondi e premere il tasto FF. "
        # TODO: Implement result: "Il playback va in Fast Forward"
        raise NotImplementedError

    def test_timeshift_scomparsa_automatica_del_banner(self):
        # Tags: Timeshift
        # TODO: Implement action: "L'utente sintonizza un canale DTT a piacere"
        # TODO: Implement action: "L'utente mette in pausa in modo da attivare il time shift"
        # TODO: Implement action: "L'utente lascia in pausa per qualche minuto"
        # TODO: Implement action: "L'utente preme nuovamente il tasto play/pausa: il flusso riprende da dove era stato fermato"
        # TODO: Implement action: "L'utente preme il pulsante FFW del telecomando e lascia andare avanti rapidamente la porzione di contenuto che era stata memorizzata tramite il timeshift. Si nota che il pilotino del player scompare ma il contenuto continua ad andare avanti veloce. Lasciarlo andare avanti così fino in fondo, in modo da risincronizzarsi con il flusso del canale"
        # TODO: Implement action: "Non appena ci si risincronizza con il flusso del canale, ricompare automaticamente il pilotino del player ma a questo punto si osserva che esso non scompare più automaticamente (occorre agire sul tasto Back del telecomando per farlo andare via)."
        # TODO: Implement result: " Il pilotino del player deve sparire"
        raise NotImplementedError
