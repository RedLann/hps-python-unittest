# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestEPGManager(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_epg_manager_test_case_1(self):
        # Tags: Enrich
        # TODO: Implement action: "Apertura immediata GridEpg all'avvio"
        # TODO: Implement action: "Connessione wifi on"
        # TODO: Implement action: "Reboot"
        # TODO: Implement result: "Tutti i canali vengono aggiornati "
        raise NotImplementedError

    def test_epg_manager_test_case_2(self):
        # Tags: Enrich
        # TODO: Implement action: "Avvio box con connessione lenta o assente"
        # TODO: Implement action: "collegamento del cavo o della wifi CON EPG APERTA "
        # TODO: Implement result: "I canali vengono aggiornati e successivamente alla prossima riapertura dell'EPG la grid è aggiornata con i canali arricchiti "
        raise NotImplementedError

    def test_epg_manager_test_case_3(self):
        # Tags: Enrich
        self.actionwords.eliminare_il_db_canali()
        # TODO: Implement action: "scansione dtt"
        # TODO: Implement result: "la rich epg è visibile nelle epg (short e grid) "
        raise NotImplementedError
