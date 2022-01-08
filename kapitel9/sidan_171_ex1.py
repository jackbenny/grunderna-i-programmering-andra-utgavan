#!/usr/bin/env python3

# alice.py, version 3

# Denna funktion ersätter lambda
def funk(x):
    return x[1]

rakna = dict()
fil = open("alice.txt")
innehall = fil.read().replace(",", " ").replace(".", " ")\
    .replace("'", " ").lower()
ord = innehall.split()

for o in ord:
    rakna[o] = rakna.get(o, 0) + 1

# key=funk ersätter lambda från förra versionen
sorterad = sorted(rakna.items(), key=funk, reverse=True)

hogsta = 0
for i, j in sorterad:
    print (i, "\t", j)
    hogsta += 1
    if hogsta == 10:
        break
