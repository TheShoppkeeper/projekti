import random

nopat = []
noppa = int(input("Anna noppien lukumäärä tai lopeta syöttämällä 0 "))
summa = 0

while noppa!=0:
    nopat.append(noppa)
    noppa = int(input("Anna noppien lukumäärä tai lopeta syöttämällä 0 "))

for noppa in nopat:
    summa += noppa*random.randint(1,6)

print(summa)
