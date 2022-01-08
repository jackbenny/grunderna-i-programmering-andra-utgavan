konton = {"Kalle": 300, "Joakim": 1800, "Lisa": 900}

hogst = 0
rikast = str()

for i, j in konton.items():
    print(i, j)
    if (hogst == 0):
        hogst = j
        rikast = i
    if (j > hogst):
        hogst = j
        rikast = i

print (rikast, "är rikast!")
