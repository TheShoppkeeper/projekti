#tee lista jossa on numerot annetun muuttujan ja yhden välillä
luku = int(input("Anna luku ja kerron onko se alkuluku: "))
lista = list(range(2,(luku)))
n = luku
check = 0
#tee for, jossa tarkistetaan jos annettu luku on jaollinen listan numerolla.

for luku in lista:
    if n % luku == 0:
        check += 1
        break

if check == 0:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")
