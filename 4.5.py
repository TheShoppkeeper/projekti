tunnus = "python"
salis = "rules"
tunnari = input("Anna käyttäjätunnus ")
salasana = input("Anna salasana ")
laskuri = 0

while True:
    if tunnus == tunnari and salis == salis:
        break
    laskuri += 1
    if laskuri == 5:
        break
    tunnari = input("Anna käyttäjätunnus uudestaan ")
    salasana = input("Anna salasana uudestaan ")

if laskuri == 5:
    print("Pääsy evätty")
else:
    print("Tervetuloa")