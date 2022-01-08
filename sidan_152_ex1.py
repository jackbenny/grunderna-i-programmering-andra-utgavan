#!/usr/bin/env python3

while True:
    try:
        tal = int(input("Skriv ett heltal: "))
    except:
        print ("Skriv endast heltal")
    else:
        print ("Du skrev", tal)
        break
