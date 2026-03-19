class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0




auto1 = Auto("ACD-445",142)
print(f"Auton rekkari on {auto1.rekisteritunnus} ja huippunopeus {auto1.huippunopeus}. Auton nopeus on {auto1.nopeus} ja kuljettu matka {auto1.matka}")