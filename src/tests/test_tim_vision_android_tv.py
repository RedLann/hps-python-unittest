# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestTIMVisionAndroidTV(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_monkey_script(self):
        # Tags: monkey
        # TODO: Implement action: "Eseguire il comando: adb shell monkey -p timvision.launcher -c android.intent.category.HOME --pct-majornav 20 --pct-nav 20 --pct-syskeys 50 --throttle 20 -v 10000 "
        # TODO: Implement result: "NO CRASH"
        raise NotImplementedError

    def test_barker_test_case_1(self):
        # Tags: Barker
        # TODO: Implement action: "Avviare la tvapp senza canali dtt in modo che venga riprodotto il barker"
        # TODO: Implement action: "Premere ok per interrompere il barker"
        # TODO: Implement result: "Il barker si interrompe e vengono mostrati o gli sfondi o il primo canale live disponibile"
        raise NotImplementedError
