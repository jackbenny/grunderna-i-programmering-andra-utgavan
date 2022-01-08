#!/usr/bin/env python3
# Valutaomräkningsprogram, version 3
import pickle

# Fråga användaren om han vill ladda en tidigare kurs
ladda = input("Vill du ladda tidigare kurs? (j/n): ")
if (ladda == "j"):

    # Påbörja felhanteringen för filöppningen
    try:
        kurs = pickle.load(open('kurs.p', 'rb'))
    # Om filen inte finns, skriv ut ett meddelande
    # och fråga användaren om en ny kurs (om och om
    # igen till tills ett tal har lästs in). Spara
    # sedan den nya kursen.
    except FileNotFoundError:
        print ("Det finns ingen tidigare sparad kurs.")
        while True:
            try:
                kurs = float(input("Ange ny USD-kurs: "))
            except ValueError:
                print ("Ange endast flyttal eller heltal")
            else:
                pickle.dump(kurs,open('kurs.p', 'wb'))
                break
    # Om vi inte har rättigheter att läsa filen, avsluta
    # och skriv ut ett felmeddelande.			
    except PermissionError:
        print ("Något är fel med rättigheterna för kurs.p")
        quit()
elif (ladda == "n"):
    # Repetera tills ett flyttal har lästs in.
    while True:
        try:
            kurs = float(input("Ange ny USD-kurs: "))
        except ValueError:
            print ("Ange endast flyttal eller heltal")
        else:
            pickle.dump(kurs,open('kurs.p', 'wb'))
            break
else:
    print ("Var god svara (j)a eller (n)ej")
    quit()

# Repetera tills ett flytttal har lästs in som SEK
while True:
    try:
        usd = float(input("Ange summa i USD: "))
    except ValueError:
        print ("Ange endast flyttal eller heltal")
    else:
        break
# Skriv ut svaret	
print ("%.2f USD motsvarar %.2f SEK" \
    %(usd, usd*kurs))
