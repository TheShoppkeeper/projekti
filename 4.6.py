import random

N = int(input("Montako testipistettä haluaisit"))
n = 0
arvo1 = 0
arvo2 = 0
kerta = 0

while kerta < N:
    arvo1 = random.uniform(-1,1)
    arvo2 = random.uniform(-1,1)
    if float((arvo1 ** 2) + (arvo2 ** 2)) < 1:
        n += 1
    kerta += 1

print((n * 4) / N)

