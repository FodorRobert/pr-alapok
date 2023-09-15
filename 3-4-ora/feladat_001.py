#feladat_001

"""
Kérjük be a billentyűzetről a nevünket, és írassuk ki a képernyőre!
A bilentyűzetről mindig szöveget (string-et) olvasunk be!
type(válttozó) --- visszaadja a változó típusát  
"""


"""
nev = input ("Kérek egy nevet: ")
print (f"A megadott név a következő: {nev}")
"""

vnev = input ("Kérek egy vezetéknevet: ")
knev = input ("kérek egy keresztnevet: ")
print (f"A megadott név a következő: {vnev} {knev}")

print (f"a vnev változó típusa: {type(vnev)}")
print (f"a knev változó típusa: {type(knev)}")