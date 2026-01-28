import math

halkaisija1 = 0.01*float(input("Anna pizzan halkaisija senttimetreinä: "))
hinta1 = float(input("Anna pizzan hinta euroina: " ))
halkaisija2 = 0.01*float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: " ))

def suhde(h,p):
    s = (math.pi*((h/2)**2))
    v = (p / s)
    return v

if suhde(halkaisija1,hinta1) < suhde(halkaisija2, hinta2):
    print("Ensimmäinen pizza on halvempi")
else:
    print("Toinen pizza on halvempi")

