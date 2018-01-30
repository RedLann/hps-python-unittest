# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestKeymapping(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_keymap_tv_button_da_altra_applicazione_con_canali_disattivati(self):
        # Tags: Keymap BTN_TV
        self.actionwords.box_state(browsable_count = "0")
        # TODO: Implement action: "Aprire un'applicazione che non sia la TVApp o App e Giochi"
        self.actionwords.press_key(key = "TV")
        # TODO: Implement result: "Viene lanciata la TVApp ma la Short EPG non viene aperta poichè disabilitata in assenza di browsabili"
        raise NotImplementedError

    def test_keymap_tv_button_durante_la_visione_di_un_programma(self):
        # Tags: Keymap BTN_TV
        # TODO: Implement action: "Sintonizzarsi su un qualsiasi canale"
        self.actionwords.press_key(key = "TV")
        # TODO: Implement result: "Si apre la Short EPG sul canale sintonizzato"
        raise NotImplementedError

    def test_keymap_back_button_su_canale_apre_grid_epg(self):
        # Tags: Keymap BTN_BACK
        # TODO: Implement action: "Con carousel chiuso, durante la visione di un qualsiasi canale"
        self.actionwords.press_key(key = "BACK")
        # TODO: Implement result: "Si apre la GRID EPG in stato Partial (tendina dei filtri espansa)"
        raise NotImplementedError

    def test_keymap_back_button_su_grid_epg_partial(self):
        # Tags: Keymap BTN_BACK
        # TODO: Implement action: "Con GRID EPG aperta in stato Partial (tendina dei filtri espansa)"
        self.actionwords.press_key(key = "BACK")
        # TODO: Implement result: "La GRID EPG viene chiusa"
        # TODO: Implement result: "Viene aperto il carousel sul canale corrente in riproduzione"
        raise NotImplementedError

    def test_keymap_back_button_su_grid_epg_full(self):
        # Tags: Keymap BTN_BACK
        # TODO: Implement action: "Con GRID EPG aperta in stato Full (tendina dei filtri collapsed)"
        self.actionwords.press_key(key = "BACK")
        # TODO: Implement result: "La tendina dei filtri passa allo stato espanso con la relativa animazione"
        # TODO: Implement result: "Viene riprodotta l'animazione Snake sul filtro correntemente selezionato"
        raise NotImplementedError

    def test_keymap_back_button_su_carousel(self):
        # Tags: Keymap BTN_BACK
        # TODO: Implement action: "Con CAROUSEL aperto"
        self.actionwords.press_key(key = "BACK")
        # TODO: Implement result: "Il CAROUSEL viene chiuso"
        raise NotImplementedError

    def test_keymap_back_button_su_short_epg(self):
        # Tags: Keymap BTN_BACK
        # TODO: Implement action: "Con Short EPG aperta"
        self.actionwords.press_key(key = "BACK")
        # TODO: Implement result: "La Short EPG viene chiusa"
        # TODO: Implement result: "Il CAROUSEL rimane chiuso"
        raise NotImplementedError

    def test_keymap_tv_button_da_altra_applicazionemenu(self):
        # Tags: Keymap BTN_TV
        # TODO: Implement action: "Aprire un'applicazione che non sia la TVApp o App e Giochi, compresi settings della TVApp e settings di Android"
        self.actionwords.press_key(key = "TV")
        # TODO: Implement result: "Viene lanciata la TVApp e viene aperta la Short EPG sul canale selezionato"
        raise NotImplementedError

    def test_keymap_tv_button_con_canali_disabilitati(self):
        # Tags: Keymap BTN_TV
        self.actionwords.box_state(firmware = "4.3.4", browsable_count = "0")
        self.actionwords.press_key(key = "TV button")
        # TODO: Implement result: "Apertura TvApp senza ShortEpg "
        raise NotImplementedError
