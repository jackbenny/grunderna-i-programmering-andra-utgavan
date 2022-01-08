#!/usr/bin/env python3

# alice.py, version 1

# Skapa en ordlista som ska användas för att räkna ord
rakna = dict()

# Öppna filen med open, läs in innehållet till 'innehall'
# och byt ut tecknen ,.' mot mellanslag. Gör sen om
# allt till små bokstäver
fil = open("alice.txt")
innehall = fil.read()
innehall = innehall.replace(",", " ").replace(".", " ")\
    .replace("'", " ").lower()

# Dela upp hela innehållet i enstaka ord i en lista
ord = innehall.split()

# Loopa igenom ord för ord. Om ordet inte redan finns
# i 'rakna' läggs det in och sätts till 1. Om det
# redan finns, addera med 1.
for o in ord:
    if (o not in rakna):
        rakna[o] = 1
    else:
        rakna[o] = rakna[o] + 1

# Vänd på nyckel och värde
omvand = dict()
for k, v in rakna.items():
    omvand[v] = k

# Sortera i omvänd ordning
sorterad = sorted(omvand.items(), reverse=True)

# Skriv ut de 10 mest frekventa orden och hur
# hur många gånger de förekommer
hogsta = 0
for i, j in sorterad:
    print (j, "\t", i)
    hogsta = hogsta + 1
    if hogsta == 10:
        break
