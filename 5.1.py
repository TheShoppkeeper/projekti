import random

nopat = []
noppa = (input("Anna noppien lukumäärä tai painamalla enter: "))
summa = 0

while noppa!="":
    nopat.append(int(noppa))
    noppa = input("Anna noppien lukumäärä tai painamalla enter: ")

for noppa in nopat:
    summa += noppa*random.randint(1,6)

print(summa)
