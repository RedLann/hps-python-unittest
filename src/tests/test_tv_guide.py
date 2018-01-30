# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestTVGuide(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_tvguide_focus_navigation_testing_uida4f8d003c171406dbf49f0dc5d4c5a54(self):
        # Tags: EPG_Grid_Focus TVGuide
        # TODO: Implement action: "Navigare sugli item della GRID EPG "
        # TODO: Implement result: "Il focus rimane sugli item della GRID EPG se non viene esplicitamente spostato il focus sui filtri (Left Arrow o Back Button) quindi non ci sono perdite di focus"
        raise NotImplementedError
