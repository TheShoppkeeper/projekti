
def muunnin(litrat):
    return litrat*3.785

gallona = float(input("Montako gallonaa sinulla on: "))

while gallona > 0:
    print(muunnin(gallona))
    gallona = float(input("Montako gallonaa sinulla on: "))