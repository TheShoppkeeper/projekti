import math

halkaisija1 = 0.01*float(input("Anna pizzan halkaisija senttimetreinä"))
hinta1 = float(input("Anna pizzan hinta euroina"))

s = (math.pi*((halkaisija1/2)**2))
v = (hinta1 / s)

print(s)
print(v)