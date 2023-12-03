KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        if kapasiteetti is not None:
            self.kapasiteetti = kapasiteetti
        if kasvatuskoko is not None:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluuko_luku_lukujonoon(self, luku):
        luvun_maara = 0

        for i in range(0, self.alkioiden_lkm):
            if luku == self.lukujono[i]:
                luvun_maara += 1

        if luvun_maara > 0:
            return True
        else:
            return False

    def lisaa_luku_jonoon(self, luku):
        if self.alkioiden_lkm == 0:
            self.lukujono[0] = luku
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        else:
            pass

        if not self.kuuluuko_luku_lukujonoon(luku):
            self.lukujono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.lukujono) == 0:
                self.kasvata_lukujonon_kokoa()

            return True

        return False
    
    def kasvata_lukujonon_kokoa(self):
        taulukko_old = self.lukujono
        self.kopioi_lista(self.lukujono, taulukko_old)
        self.lukujono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(taulukko_old, self.lukujono)

    def poista_luku(self, luku):
        luvun_kohta = -1
        korvaava_luku = 0

        for i in range(0, self.alkioiden_lkm):
            if luku == self.lukujono[i]:
                luvun_kohta = i
                self.lukujono[luvun_kohta] = 0
                break

        if luvun_kohta != -1:
            for j in range(luvun_kohta, self.alkioiden_lkm - 1):
                korvaava_luku = self.lukujono[j]
                self.lukujono[j] = self.lukujono[j + 1]
                self.lukujono[j + 1] = korvaava_luku

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_lista(self, lista1, lista2):
        for i in range(0, len(lista1)):
            lista2[i] = lista1[i]

    def joukon_mahtavuus(self):
        return self.alkioiden_lkm

    def luo_numerolista(self):
        numerolista = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(numerolista)):
            numerolista[i] = self.lukujono[i]

        return numerolista

    @staticmethod
    def yhdiste(jono1, jono2):
        joukko = IntJoukko()
        a_taulu = jono1.luo_numerolista()
        b_taulu = jono2.luo_numerolista()

        for i in range(0, len(a_taulu)):
            joukko.lisaa_luku_jonoon(a_taulu[i])

        for i in range(0, len(b_taulu)):
            joukko.lisaa_luku_jonoon(b_taulu[i])

        return joukko

    @staticmethod
    def leikkaus(jono1, jono2):
        joukko = IntJoukko()
        a_taulu = jono1.luo_numerolista()
        b_taulu = jono2.luo_numerolista()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    joukko.lisaa_luku_jonoon(b_taulu[j])

        return joukko

    @staticmethod
    def erotus(jono1, jono2):
        joukko = IntJoukko()
        a_taulu = jono1.luo_numerolista()
        b_taulu = jono2.luo_numerolista()

        for i in range(0, len(a_taulu)):
            joukko.lisaa_luku_jonoon(a_taulu[i])

        for i in range(0, len(b_taulu)):
            joukko.poista_luku(b_taulu[i])

        return joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
