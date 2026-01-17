leviska = float(input("Anna leviskät "))
naulat = float(input("Anna naulat "))
luodit = float(input("Anna luodit "))

massa = ((leviska*20*32*0.0133)+(naulat*32*0.0133)+(luodit*0.0133))
kilo = int(massa)
grammat = ((massa-kilo)*1000)

print("Massa nykymittojen mukaan")
print(f"{kilo} kilogrammaa ja {grammat:0.2f} grammaa.")
