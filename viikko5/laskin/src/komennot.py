class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self.sovellus = sovelluslogiikka
        self.syote = syote
        self.alkuperainen_arvo = 0

    def suorita(self):
        self.alkuperainen_arvo = self.sovellus.arvo()
        self.sovellus.plus(self.syote())

    def kumoa(self):
        self.sovellus.aseta_arvo(self.alkuperainen_arvo)

class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovellus = sovelluslogiikka
        self.syote = syote
        self.alkuperainen_arvo = 0

    def suorita(self):
        self.alkuperainen_arvo = self.sovellus.arvo()
        self.sovellus.miinus(self.syote())

    def kumoa(self):
        self.sovellus.aseta_arvo(self.alkuperainen_arvo)

class Nollaus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovellus = sovelluslogiikka
        self.syote = syote
        self.alkuperainen_arvo = 0

    def suorita(self):
        self.alkuperainen_arvo = self.sovellus.arvo()
        self.sovellus.nollaa()

    def kumoa(self):
        self.sovellus.aseta_arvo(self.alkuperainen_arvo)
