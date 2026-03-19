class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytys(self,kiihdytys):
        self.nopeus += kiihdytys
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0


auto1 = Auto("ACD-445",142)
auto1.kiihdytys(30)
auto1.kiihdytys(70)
auto1.kiihdytys(50)
print(f"Auton nopeus on {auto1.nopeus}kmh")
auto1.kiihdytys(-200)
print(f"Auton nopeus on {auto1.nopeus}kmh")