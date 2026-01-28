import random
def heitto():
    return random.randint(1,6)

noppa = heitto()
print(noppa)

while True:
    if noppa == 6:
        break
    heitto()
    noppa = heitto()
    print(noppa)