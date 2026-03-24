class Hissi:
    def __init__(self, hissinumero, alakerros, ylakerros):
        self.hissinumero = hissinumero
        self.alakerros = alakerros
        self.ylakerros = ylakerros
        self.kerros = 1

    def kerros_alas(self):
        self.kerros -= 1

    def kerros_ylös(self):
        self.kerros += 1

    def siirry_kerrokseen(self,mihin):
        print(f"Olet nyt kerroksessa {self.kerros}")
        while self.kerros != mihin:
            if self.kerros > mihin:
                self.kerros -= 1
                print(f"Olet nyt kerroksessa {self.kerros}")
            elif self.kerros < mihin:
                self.kerros += 1
                print(f"Olet nyt kerroksessa {self.kerros}")



class Talo:
    def __init__(self,ylinkerros, alinkerros,hissit):
        self.ylinkerros = ylinkerros
        self.alinkerros = alinkerros
        self.hissit = []
        for i in range(1,hissit+1):
            self.hissit.append(Hissi(i,alinkerros, ylinkerros))
    def aja_hissiä(self, hissinumero, kohdekerros):
        hissi1 = self.hissit[(hissinumero-1)]
        hissi1.siirry_kerrokseen(kohdekerros)

talo1 = Talo(7,1,3)
talo1.aja_hissiä(3,7)
