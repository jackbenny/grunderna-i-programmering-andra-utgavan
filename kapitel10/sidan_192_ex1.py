#!/usr/bin/env python3

import urllib.request

# Vi börjar med att skapa ett objekt
url = urllib.request.urlopen\
    ("http://jackbenny.se/test.html")

# Nu läser vi in HTML-dokumentet
html = url.read()

# Därefter måste vi omkoda byte till en sträng för att
# t.ex. radbrytningar ska fungera korrekt
htmlUtf = html.decode("utf-8")

# Visa HTML-dokumentet
print (htmlUtf)
