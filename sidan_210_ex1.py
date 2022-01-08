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
