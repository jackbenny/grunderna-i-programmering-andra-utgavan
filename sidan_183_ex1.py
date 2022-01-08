#!/usr/bin/env python3
import datetime

veckodagar = ["måndag", "tisdag", "onsdag",
                "torsdag", "fredag", "lördag",
                "söndag"]

ar = int(input("Ange år med fyra tecken: "))

print ("Julafton år", str(ar), "är en",
veckodagar[datetime.date(ar, 12, 24).weekday()])
