import random
jackpot = random.randint(1,10)
arvaus = int(input("Arvaa luku yhden ja kymmenen välillä "))
while jackpot > arvaus or jackpot < arvaus:
    if jackpot < arvaus:
        print("liian suuri arvaus")
        arvaus = int(input("Arvaa luku uudestaan "))
    elif jackpot > arvaus:
        print("Liian pieni arvaus")
        arvaus = int(input("Arvaa luku uudestaan "))
    else:
        print("Vastaa numero yhden ja kymmenen välillä")


print("oikea vastaus")