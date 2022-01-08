#!/usr/bin/env python3

import math

try:
    t = int(input("Ange täljaren: "))
    n = int(input("Ange nämnaren: "))
except ValueError:
    exit("Ange endast heltal")

sgd = math.gcd(t, n)

print ("SGD är:", str(sgd))
print (str(t) + "/" + str(n), "=", \
        str(int(t/sgd)) + "/" + str(int(n/sgd)))
