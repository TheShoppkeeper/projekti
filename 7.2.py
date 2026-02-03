nimet = set()
nimi = input("Anna nimi tai lopeta painamalla enter:")
while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        nimet.add(nimi)
    nimi = input("Anna nimi tai lopeta painamalla enter:")

for nimi in nimet:
    print(nimi)