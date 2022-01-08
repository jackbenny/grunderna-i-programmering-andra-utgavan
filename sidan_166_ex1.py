#!/usr/bin/env python3

var = "Lisa"

def funk1():
    var = "Kalle"
    return var

var = "Anna"

print ("Inuti funk1 är 'var':", funk1())
print ("Globalt är 'var':", var)
