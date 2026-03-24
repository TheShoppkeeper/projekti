class Hissi:
    def __init__(self, alakerros, ylakerros):
        self.alakerros = alakerros
        self.ylakerros = ylakerros
        self.kerros = 1

    def kerros_alas(self):
        self.kerros -= 1

    def kerros_ylös(self):
        self.kerros += 1

    def siirry_kerrokseen(self,mihin):
        while self.kerros != mihin:
            if self.kerros > mihin:
                self.kerros -= 1
                print(f"Olet nyt kerroksessa {self.kerros}")
            elif self.kerros < mihin:
                self.kerros += 1
                print(f"Olet nyt kerroksessa {self.kerros}")




hissi1 = Hissi(1,7)
hissi1.siirry_kerrokseen(7)
hissi1.siirry_kerrokseen(1)