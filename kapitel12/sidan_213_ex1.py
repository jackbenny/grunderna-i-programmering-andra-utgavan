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
