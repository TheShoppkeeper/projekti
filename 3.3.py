sukupuoli = input("Anna sukupuolesi ")
hemogoblin = int(input("Anna hemoglobiini arvosi "))

if sukupuoli == "mies" and 134<=hemogoblin<=195 or sukupuoli == "nainen" and 117<=hemogoblin<=175:
    print("Hemoglobiiniarvo on normaali")
elif sukupuoli == "mies" and hemogoblin > 195 or sukupuoli == "nainen" and hemogoblin > 175:
    print("Hemoglobiiniarvo on korkea")
else:
    print("Hemoglobiiniarvo on alhainen")