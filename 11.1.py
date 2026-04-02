class julkaisu:
    def __init__(self, name):
        self.name = name

    def tulosta(self):
        print(f"{self.name}")

class lehti(julkaisu):
    def __init__(self, name, toimittaja):
        self.toimittaja = toimittaja
        super().__init__(name)

    def tulosta(self):
        super().tulosta()
        print(f"{self.toimittaja}")

class kirja(julkaisu):
    def __init__(self, name, sivut, kirjailija):
        self.sivut = sivut
        self.kirjailija = kirjailija
        super().__init__(name)

    def tulosta(self):
        super().tulosta()
        print(f"{self.kirjailija} {self.sivut}")


Aku = lehti("Aku ankka", "Aki Hyyppä")
Hyttin06 = kirja("Hyttino6",200,"Rosa Liksom")

Aku.tulosta()
Hyttin06.tulosta()