# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_home_page_componenti_home_page(self):
        # TODO: Implement action: "Precondizioni: rete internet"
        # TODO: Implement action: "Accedere alla Home Page della TvApp"
        # TODO: Implement result: "La Home è composta da:
        # -Barra di stato (parte alta dello schermo), dove viene posizionato il logo TIM a sinistra, e al centro l’orario e alcune icone di stato: mute, assenza di rete, batteria telecomando scarica…
        #  -Menu (parte bassa dello schermo), per consentire l’accesso a Settings e search a sinistra, guida tv, tim vision e app e giochi nel settore di destra"
        raise NotImplementedError

    def test_home_page_componenti_home_page_no_rete(self):
        # TODO: Implement action: "Precondizioni: rete internet assente"
        # TODO: Implement action: "Accedere alla Home Page della TvApp"
        # TODO: Implement result: "In caso di mancanza di connessione il menu dovrà garantire l’accesso a “Settings”, \"\"guida tv\"\" e ”app e giochi” Anche la Search compare solo se c'è connessione"
        # TODO: Implement result: "In caso di mancanza di connessione nella barra di stato non dovrà essere presente l'informazione relativa all'orario"
        raise NotImplementedError

    def test_home_page_componenti_home_pageno_icona_rete_se_connnessa_tramite_ethernet(self):
        # TODO: Implement action: "Precondizioni: ethernet"
        # TODO: Implement action: "Accedere alla Home Page della TvApp"
        # TODO: Implement result: "Non viene visualizzata alcuna icona relativa al WiFI (né connessione attiva, né connessione disattiva)"
        raise NotImplementedError

    def test_home_page_componenti_home_pageicone_di_stato_non_cliccabili(self):
        # TODO: Implement action: "Accedere alla Home Page della TvApp"
        # TODO: Implement action: "Spostarsi con le frecce sulle icone della barra di stato"
        # TODO: Implement result: "Le icone della barra di stato non sono cliccabili né navigabili, non può essere possibile spostare il cursore sopra esse"
        raise NotImplementedError

    def test_home_page_zapping_sulla_home_page(self):
        # TODO: Implement action: "Precondizioni: canali presenti "
        # TODO: Implement action: "Accedere alla Home Page della TvApp"
        # TODO: Implement action: "Premere i pulsanti P+, P- e tastierino numerico"
        # TODO: Implement result: "Sparisce la Home Page e appare la Short Epg"
        raise NotImplementedError

    def test_home_page_canali_presentichiusura_menu(self):
        # TODO: Implement action: "Accedere alla Home Page della TvApp"
        # TODO: Implement action: "Premere il tasto tasto Home o il tasto back"
        # TODO: Implement result: "Chiusura del menù, continua visualizzazione dell'ultimo canale visualizzato"
        raise NotImplementedError

    def test_home_page_no_canalichiusura_menu(self):
        # TODO: Implement action: "Precondizioni: 
        # -rete internet
        # -canali assenti"
        # TODO: Implement action: "Accedere alla Home Page della TvApp"
        # TODO: Implement action: "Premere il tasto tasto Home o il tasto back"
        # TODO: Implement result: "Chiusura del menù visualizzazione sfondo di default (se immagine custom non configurata)"
        raise NotImplementedError

    def test_home_page_bootcanali_presenti(self):
        # TODO: Implement action: "Precondizioni: canali dtt presenti"
        self.actionwords.reboot()
        # TODO: Implement result: "Accesso alla Home Page della TvApp"
        # TODO: Implement result: "Play ultimo canale sintonizzato con menù aperto"
        raise NotImplementedError

    def test_home_page_bootvisualizzazione_barker_sfondi_e_canali(self):
        # TODO: Implement action: "Precondizioni: 
        # -rete internet
        # -canali dtt assenti"
        self.actionwords.reboot()
        # TODO: Implement result: "Accesso alla Home Page della TvApp"
        # TODO: Implement result: "Visualizzazione barker con menù aperto. A video terminato:
        # - sintonizzazione sull'ultimo canale sintonizzato se sono presenti canali non dtt; 
        # -visualizzazione sfondo di default (se immagine custom non configurata) con menù aperto"
        raise NotImplementedError

    def test_home_page_bootno_rete_no_dtt(self):
        # TODO: Implement action: "Precondizioni:
        # -no rete internet
        # -no canali"
        self.actionwords.reboot()
        # TODO: Implement result: "Accesso alla Home Page della TvApp"
        # TODO: Implement result: "Visualizzazione sfondi di default con menù aperto (si chiude dopo mancata interazione col telecomando)"
        raise NotImplementedError

    def test_home_page_avvio_dopo_standby(self):
        # TODO: Implement action: "Precondizioni:
        # -canali presenti"
        # TODO: Implement action: "Accedere alla Home Page della TvApp"
        self.actionwords.standby_on__off()
        # TODO: Implement result: "Play ultimo canale sintonizzato con menù aperto (si chiude dopo mancata interazione col telecomando)"
        raise NotImplementedError

    def test_home_page_avvio_dopo_standby_no_canali(self):
        # TODO: Implement action: "Precondizioni: 
        # -rete internet
        # -canali assenti"
        # TODO: Implement action: "Accedere alla Home Page della TvApp"
        self.actionwords.standby_on__off()
        # TODO: Implement result: "Visualizzazione sfondo di default (se immagine custom non configurata) con menù aperto (si chiude dopo mancata interazione col telecomando)"
        raise NotImplementedError

    def test_home_page_avvio_dopo_standby_no_rete_no_canali(self):
        # TODO: Implement action: "Precondizioni:
        # -no rete internet
        # -canali assenti"
        # TODO: Implement action: "Accedere alla Home Page della TvApp"
        self.actionwords.standby_on__off()
        # TODO: Implement result: "Visualizzazione sfondi di default con menù aperto (si chiude dopo mancata interazione col telecomando)"
        raise NotImplementedError

    def show_carousel(self, connection, connection_after, carousel_type):
        # TODO: Implement action: "Condizione iniziale %s" % (connection)
        # TODO: Implement action: "passare allo stato %s" % (connection_after)
        # TODO: Implement action: "Il carosello da visualizzare è quello %s" % (carousel_type)
        raise NotImplementedError

    def test_Show_Carousel_1(self):
        self.show_carousel(connection = 'wifi on', connection_after = 'wifi off', carousel_type = 'carousel offline')

    def test_Show_Carousel_2(self):
        self.show_carousel(connection = 'wifi off', connection_after = 'wifi on', carousel_type = 'carousel online')

    def test_Show_Carousel_3(self):
        self.show_carousel(connection = 'eth on', connection_after = 'eth off', carousel_type = 'carousel offline')

    def test_Show_Carousel_4(self):
        self.show_carousel(connection = 'eth off', connection_after = 'eth on', carousel_type = 'carousel online')
