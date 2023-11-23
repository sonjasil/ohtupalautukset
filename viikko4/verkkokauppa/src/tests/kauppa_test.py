import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegen_mock = Mock()
        self.varasto_mock = Mock()
        self.saldot = {}

        self.viitegen_mock.uusi.return_value = 42

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 5
            elif tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                tuote = Tuote(1, "maito", 5)
                self.saldot[tuote] = varasto_saldo(tuote_id)
                return tuote
            elif tuote_id == 2:
                tuote = Tuote(2, "jauho", 3)
                self.saldot[tuote] = varasto_saldo(tuote_id)
                return tuote
            elif tuote_id == 3:
                tuote = Tuote(3, "keksit", 2)
                self.saldot[tuote] = varasto_saldo(tuote_id)
                return Tuote
            
        def varasto_poista_tuote(tuote):
            self.saldot[tuote] -= 1
            return self.saldot[tuote]
        
        def varasto_lisaa_tuote(tuote):
            self.saldot[tuote] += 1
            return self.saldot[tuote]

        
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegen_mock)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.varasto_mock.ota_varastosta.side_effect = varasto_poista_tuote
        self.varasto_mock.palauta_varastoon.side_effect = varasto_lisaa_tuote
    
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_kutsutaan_tilisiirtoa_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_ostetaan_kaksi_eri_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 8)

    def test_ostetaan_kaksi_samaa_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

    def test_ostetaan_toisena_tuotteena_loppunut_tuote(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 3)

    def test_hinta_nollautuu_ostosten_valissa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", "33333-44455", 3)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("heli", "67890")

        self.pankki_mock.tilisiirto.assert_called_with("heli", ANY, "67890", "33333-44455", 5)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("ville", "13579")

        self.pankki_mock.tilisiirto.assert_called_with("ville", ANY, "13579", "33333-44455", 0)

    def test_uusi_viite_jokaiselle_maksulle(self):
        viite_mock = Mock(wraps=Viitegeneraattori())
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, viite_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        self.assertEqual(viite_mock.uusi.call_count, 1)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("heli", "67890")

        self.assertEqual(viite_mock.uusi.call_count, 2)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("ville", "13579")

        self.assertEqual(viite_mock.uusi.call_count, 3)

    def test_korista_poisto_palauttaa_tuotteen_varastoon(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("pekka", "12345")

        tuote = self.varasto_mock.hae_tuote(2)

        self.assertEqual(self.saldot[tuote], 5)