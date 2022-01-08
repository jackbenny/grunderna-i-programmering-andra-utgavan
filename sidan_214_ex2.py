#!/usr/bin/env python3

import urllib.request

# Be användaren om en adress
adress = input("Ange adress till loggfilen: ")

# Om adressen är kortare än ett tecken angav
# användaren ingen adress, så vi kör på default
if (len(adress) < 1):
    adress = "http://jackbenny.se/logg.txt"

# Try-block för att testa om adressen finns och är
# giltig.
try:
    # Vi börjar med att skapa ett objekt
    url = urllib.request.urlopen\
            (adress)
except ValueError:
    quit("Ogiltigt adressformat")
except urllib.error.URLError:
    quit("Fel eller okänd adress")
except urllib.error.HTTPError:
    quit("Fel adress, det finns inget där")

# Nu läser vi in loggfilen
loggfil = url.read()

# Därefter måste vi omkoda byte till en sträng för att
# t.ex. radbrytningar ska fungera korrekt
loggfilUtf = loggfil.decode("utf-8")

# Testa ifall det är loggfil och om inte, avsluta.
if "]:" not in loggfilUtf:
    quit("Det där verkar inte vara en loggfil")

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
