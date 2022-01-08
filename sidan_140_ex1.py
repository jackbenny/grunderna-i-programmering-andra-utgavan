#!/usr/bin/env python3

# alice.py, version 2

# Skapa en ordlista som ska användas för att räkna ord
rakna = dict()

# Öppna filen med open, läs in innehållet till 'innehall'
# och byt ut tecknen ,.' mot mellanslag samt gör om allt
# till små bokstäver.
fil = open("alice.txt")
innehall = fil.read().replace(",", " ").replace(".", " ")\
    .replace("'", " ").lower()

# Dela upp hela innehållet i enstaka ord i en lista
ord = innehall.split()

# Loopa igenom ord för ord, om ordet inte redan finns lägg
# in ordet, sätt standardvärde 0 och addera 1. Om ordet
# redan finns, addera bara 1 till ordet.
for o in ord:
    rakna[o] = rakna.get(o, 0) + 1

# Specialfunktion som gör att nyckeln hämtas från en ny
# egen funktion och returneras direkt från ordlistan
# (värdet).
sorterad = sorted(rakna.items(), key=lambda x: x[1], \
    reverse=True)

# Skriv ut de 10 mest förekomna orden tillsammans med
# antalet.
hogsta = 0
for i, j in sorterad:
    print (i, "\t", j)
    hogsta += 1
    if hogsta == 10:
        break
