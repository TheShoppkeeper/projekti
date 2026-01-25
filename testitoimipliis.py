import random

N = 100000
n = 0
pii = (4*n)/N
arvo1 = 0
arvo2 = 0

arvo1 = random.uniform(-1,1)
arvo2 = random.uniform(-1,1)

kerta = float((arvo1 ** 2) + (arvo2 ** 2))

print(kerta)
