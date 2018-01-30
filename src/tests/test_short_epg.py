# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestShortEPG(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_shortepg_no_db__no_shortepg(self):
        # Tags: ShortEPG
        self.actionwords.eliminare_il_db_canali()
        # TODO: Implement action: "Provare ad aprire la ShortEPG, con uno dei metodi previsti."
        # TODO: Implement result: "La ShortEPG non deve aprirsi"
        raise NotImplementedError

    def test_shortepg_show_shortepg_down(self):
        # Tags: ShortEPG DOWN
        self.actionwords.eliminare_il_db_canali()
        self.actionwords.browsable_count_n(n = "0")
        self.actionwords.press_key(key = "HOME")
        # TODO: Implement result: "La schermata HOME viene mostrata"
        self.actionwords.press_key(key = "DOWN")
        # TODO: Implement result: "La schermata ShortEPG viene mostrata"
        raise NotImplementedError

    def test_shortepg_show_shortepg_up(self):
        # Tags: ShortEPG UP
        self.actionwords.eliminare_il_db_canali()
        self.actionwords.browsable_count_n(n = "1+")
        self.actionwords.press_key(key = "HOME")
        # TODO: Implement result: "La schermata HOME viene mostrata"
        self.actionwords.press_key(key = "DOWN")
        # TODO: Implement result: "La schermata ShortEPG viene mostrata"
        raise NotImplementedError

    def test_shortepg_show_shortepg_p(self):
        # Tags: ShortEPG
        self.actionwords.eliminare_il_db_canali()
        self.actionwords.browsable_count_n(n = "1")
        self.actionwords.press_key(key = "HOME")
        # TODO: Implement result: "La schermata HOME viene mostrata"
        self.actionwords.press_key(key = "P+")
        # TODO: Implement result: "La schermata ShortEPG viene mostrata"
        raise NotImplementedError

    def test_shortepg_show_shortepg_p(self):
        # Tags: ShortEPG
        self.actionwords.eliminare_il_db_canali()
        self.actionwords.browsable_count_n(n = "1+")
        self.actionwords.press_key(key = "HOME")
        # TODO: Implement result: "La schermata HOME viene mostrata"
        self.actionwords.press_key(key = "P-")
        # TODO: Implement result: "La schermata ShortEPG viene mostrata"
        raise NotImplementedError

    def test_shortepg_browse_shortepg_updown(self):
        # Tags: ShortEPG
        self.actionwords.browsable_count_n(n = "2")
        # TODO: Implement action: "Open ShortEPG con una delle possibili modalità"
        self.actionwords.press_key(key = "UP oppure DOWN")
        # TODO: Implement result: "E' possibile navigare la ShortEPG, selezionando il CANALE precedente o successivo"
        # TODO: Implement result: "Non avviene la sintonizzazione sul CANALE selezionato"
        raise NotImplementedError

    def test_shortepg_browse_shortepg_leftright(self):
        # Tags: ShortEPG
        self.actionwords.browsable_count_n(n = "1")
        # TODO: Implement action: "Open ShortEPG con una delle possibili modalità"
        self.actionwords.press_key(key = "LEFT oppure RIGHT")
        # TODO: Implement result: "E' possibile navigare la ShortEPG, verso il PROGRAMMA precedente o successivo"
        raise NotImplementedError

    def test_shortepg_browse_shortepg_pp(self):
        # Tags: ShortEPG
        self.actionwords.browsable_count_n(n = "2")
        # TODO: Implement action: "Open ShortEPG con una delle possibili modalità"
        self.actionwords.press_key(key = "P+ oppure P-")
        # TODO: Implement result: "E' possibile navigare la ShortEPG, selezionando il CANALE precedente o successivo"
        # TODO: Implement result: "Avviene la sintonizzazione sul CANALE selezionato"
        raise NotImplementedError
