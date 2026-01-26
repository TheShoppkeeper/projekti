kaupungit = []
n = 0
#pitää keksiä miten saan for loopin toistumaan kunnes kaupungit listassa on 5 nimeä
for i in range(5):
    kaupunki = input("Anna kaupungin nimi")
    kaupungit.append(kaupunki)
    n += 1

for kaupunki in kaupungit:
    print(kaupunki)