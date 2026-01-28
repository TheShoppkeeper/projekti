lista = list(range(2,22))
def lasku(i):
    n = []
    for numero in i:
        if numero % 2 == 0:
            n.append(numero)
    return n

print(lasku(lista))
