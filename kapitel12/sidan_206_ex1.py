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

print (loggfilUtf)
