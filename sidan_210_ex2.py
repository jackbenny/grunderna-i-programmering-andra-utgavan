#!/usr/bin/env python3

import urllib.request

# Vi börjar med att skapa ett objekt
url = urllib.request.urlopen\
    ("http://jackbenny.se/logg.txt")

# Nu läser vi in loggfilen
loggfil = url.read()

# Därefter måste vi omkoda byte till en sträng för att
# t.ex. radbrytningar ska fungera korrekt
loggfilUtf = loggfil.decode("utf-8")

# Dela upp strängen i enstaka rader istället
rader = loggfilUtf.splitlines()

raknare = 0 # Räknare till antalet försök
ipLista = list() # I denna sparar vi IP-adresser
for rad in rader:
    if "Invalid user" not in rad: # INTE har söksträngen
        continue # hoppas över.
    raknare = raknare + 1 # Addera 1 till antalet försök
    ord = rad.split() # Dela upp raden i enskilda ord
    ip = ord[9] # Fält 9 är IP-adressen
    if ip not in ipLista: # Om inte adressen redan finns,
        ipLista.append(ip) # så lägg till den

# Skriv ut resultatet på skärmen
print ("\nTotalt antal försök:", raknare)
print ("\nLista över IP-adresser")
for adress in ipLista:
    print (adress)
