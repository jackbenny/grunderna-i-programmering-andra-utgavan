#!/usr/bin/env python3

def ranta(kr, ranta=2, ar=1):
    ranta = (ranta / 100) + 1
    svar = kr*ranta**ar
    return (svar)

print(ranta(55000))
