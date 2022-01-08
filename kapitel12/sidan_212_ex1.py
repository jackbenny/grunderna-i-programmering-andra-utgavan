# Be användaren om en adress
adress = input("Ange adress till loggfilen: ")

# Om adressen är kortare än ett tecken angav
# användaren ingen adress, så vi kör på default
if (len(adress) < 1):
    adress = "http://jackbenny.se/logg.txt"
