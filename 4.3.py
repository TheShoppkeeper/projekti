num = input("Anna luku ")
min = (num)
max = (num)

while num > "":
    if (num) > max:
        max = num
    elif num < min:
        min = num
    num = (input("Anna luku "))

print("Pienin luku oli " + str(min) + " ja suurin luku oli " + str(max))