leviska = float(input("Anna leviskät "))
naulat = float(input("Anna naulat "))
luodit = float(input("Anna luodit "))

massa = ((leviska*20*32*0.0133)+(naulat*32*0.0133)+(luodit*0.0133))
print(f"Paino kilogrammoina {massa:2.0f}")
