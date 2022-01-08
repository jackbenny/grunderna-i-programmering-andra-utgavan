#!/usr/bin/env python3

def ranta(kr, ranta, ar):
    ranta = (ranta / 100) + 1
    svar = kr*ranta**ar
    print (svar)

pengar = float(input("Ange hur mycket pengar du \
har på kontot: "))
procentRanta = float(input("Ange ränta i procent: "))
antalAr = float(input("Hur många år ska pengarna stå \
på kontot? "))

ranta(ar = antalAr, ranta = procentRanta, kr = pengar)
