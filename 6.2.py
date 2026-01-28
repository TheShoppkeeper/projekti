import random
n = int(input("Montako tahkoisen nopan haluaisit"))
def heitto(tahkot):
    return random.randint(1,tahkot)

noppa = heitto(n)
print(noppa)

while True:
    if noppa == n:
        break
    heitto(n)
    noppa = heitto(n)
    print(noppa)