import random
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

    def kulje(self, aika):
        self.matka += int(aika * self.nopeus)

list = []
for i in range(1,11):
    rekkari = "ABC"+str(i)
    huippunopeus = random.randint(100,200)
    list.append(Auto(rekkari, huippunopeus))
i = 0
while True:
    for auto in list:
        auto.kiihdytys(random.randint(-10,15))
        if auto.matka > 10000:
            i = 1
        auto.kulje(1)
    if i == 1:
        break


for auto in list:
    print(f"-I-  Auton rekkari on {auto.rekisteritunnus}.  -I-  Huippinopeus {auto.huippunopeus}.  -I-  Nopeus {auto.nopeus} Kuljettu matka {auto.matka}  -I-" )