class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self.sovellus = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        self.sovellus.plus(self.syote())

class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovellus = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        self.sovellus.miinus(self.syote())

class Nollaus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovellus = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        self.sovellus.nollaa()

class Kumoa:
    pass
