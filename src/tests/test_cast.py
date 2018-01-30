# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestCast(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def cast_wake_on_cast(self, fw):
        self.actionwords.box_state(firmware = "%s" % (fw), power = "Standby/Low power")
        # TODO: Implement result: "La box si accende e viene avviata la Google Cast Activity"
        raise NotImplementedError

    def test_Cast_Wake_on_cast_415(self):
        self.cast_wake_on_cast(fw = '4.1.5')

    def test_Cast_Wake_on_cast_432c(self):
        self.cast_wake_on_cast(fw = '4.3.2C')

    def test_Cast_Wake_on_cast_434(self):
        self.cast_wake_on_cast(fw = '4.3.4')



    def cast_google_cast(self, fw):
        self.actionwords.box_state(firmware = "%s" % (fw))
        # TODO: Implement result: "Viene avviata la Google Cast Activity"
        raise NotImplementedError

    def test_Cast_Google_Cast_415(self):
        self.cast_google_cast(fw = '4.1.5')

    def test_Cast_Google_Cast_432c(self):
        self.cast_google_cast(fw = '4.3.2C')

    def test_Cast_Google_Cast_434(self):
        self.cast_google_cast(fw = '4.3.4')
