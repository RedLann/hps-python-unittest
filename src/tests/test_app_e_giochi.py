# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestAppEGiochi(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_app_e_giochi_visualizzazione_app_su_2_righe(self):
        # Tags: apps_launcher
        # TODO: Implement action: "Stato: 14 app installate (esclusi giochi)"
        # TODO: Implement action: "Installare la 15° app"
        # TODO: Implement result: "Le app verranno visualizzate su due righe: 7 sulla prima riga e 8 sulla seconda"
        # TODO: Implement result: "La 15° app è l'ultima della seconda riga"
        raise NotImplementedError

    def test_app_e_giochi_visualizzazione_app_su_una_riga(self):
        # Tags: apps_launcher
        # TODO: Implement action: "Stato: 15 app installate (esclusi giochi)"
        # TODO: Implement action: "Andare sui settings della TVAPP -> Impostazioni -> App -> App scaricate"
        # TODO: Implement action: "Disinstallare una app"
        # TODO: Implement action: "Tornare su App e Giochi"
        # TODO: Implement result: "Visualizzazione delle app su una sola riga"
        raise NotImplementedError

    def test_app_e_giochi_cambio_posizione_app_dopo_ordinamento_recency(self):
        # Tags: apps_launcher
        # TODO: Implement action: "Stato: le app sono visualizzate su 2 righe, l'ordinamento è per data di installazione"
        # TODO: Implement action: "Aprire una app della seconda riga"
        # TODO: Implement action: "Sui settings della TVAPP cambiare l'ordinamento delle app (in base all'utilizzo recente)"
        # TODO: Implement action: "Tornare su App e Giochi"
        # TODO: Implement result: "Cambia l'ordinamento delle app: quella aperta al punto 2 è la prima della prima riga"
        # TODO: Implement result: "Se è stata aperta una sola app l'ultima app della prima riga diventa la prima app della seconda riga, altrimenti le app si riordinano in base all'utilizzo"
        raise NotImplementedError

    def test_app_e_giochi_cambio_posizione_app_dopo_ordinamento_fisso(self):
        # Tags: apps_launcher
        # TODO: Implement action: "Stato: le app sono visualizzate su 2 righe e sono ordinate in base all'utilizzo"
        # TODO: Implement action: "Da App e Giochi tornare sulla TVAPP e cambiare l'ordinamento delle app in base alla data di installazione"
        # TODO: Implement action: "Tornare su App e Giochi"
        # TODO: Implement result: "Le app si riordinano in base all data di installazione (focus sulla prima app consigliata da TIM)"
        raise NotImplementedError

    def test_app_e_giochi_stato_focus_al_ritorno_su_app_e_giochi_ordinamento_fisso(self):
        # Tags: apps_launcher
        # TODO: Implement action: "Stato: app ordinate in base all'ordine di installazione"
        # TODO: Implement action: "Aprire una app"
        # TODO: Implement action: "premere il tasto Back sul telecomando"
        # TODO: Implement action: "Se si è fatto ritorno sulla TVAPP tornare su App e Giochi"
        # TODO: Implement result: "Si torna su App e Giochi con il focus sulla app aperta al punto 2"
        raise NotImplementedError

    def test_app_e_giochi_stato_focus_al_ritorno_su_app_e_giochi_ordinamento_recency(self):
        # Tags: apps_launcher
        # TODO: Implement action: "Stato: app ordinate in base all'utilizzo recente"
        # TODO: Implement action: "Aprire una app"
        # TODO: Implement action: "premere il tasto Back sul telecomando"
        # TODO: Implement action: "Se si è fatto ritorno sulla TVAPP tornare su App e Giochi"
        # TODO: Implement result: "Si torna su App e Giochi con il focus sulla app aperta al punto 2. L'app si è spostata (è la prima della prima riga)"
        raise NotImplementedError

    def test_app_e_giochi_update_app_consigliate_da_tim(self):
        # Tags: apps_launcher
        # TODO: Implement action: "Stato: Netflix è installato e si trova tra le app consigliate da TIM"
        # TODO: Implement action: "Andare sui settings della TVAPP -> Impostazioni -> App -> App scaricate -> Netflix"
        # TODO: Implement action: "Disinstallare Netflix"
        # TODO: Implement action: "Aprire il Play Store e installare Netflix"
        # TODO: Implement action: "Prima della fine dell'installazione tornare su App e Giochi"
        # TODO: Implement result: "Netflix non si trova tra le app consigliate da TIM"
        # TODO: Implement result: "Alla fine dell'installazione la strip delle app consigliate da TIM si aggiorna e Netflix appare nella stessa posizione in cui si trovava al punto 1"
        raise NotImplementedError
