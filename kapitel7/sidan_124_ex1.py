antal = 0
summa = 0

while True:
    x = input("Ange tal: ")
    if (x == "klar"):
        break
    x = float(x)
    summa = summa + x
    antal = antal + 1

print ("Medelvärdet är %.1f" %(summa/antal))
