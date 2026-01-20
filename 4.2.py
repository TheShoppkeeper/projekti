tuuma = int(input("Anna tuumien määrä "))
while tuuma >= 0:
    print(str(tuuma) + " tuumaa on " + str(tuuma * 2.54) + " senttimetriä")
    tuuma = int(input("Anna tuumien määrä "))

print("En laske negatiivisia tuumia")