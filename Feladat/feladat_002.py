#feladat_002

'''
 Kérjük be a billentyűzetről két egész számot és
 írassuk ki a két szám összegét a képernyőre
'''

 
szam_1 = int(input("Kérek egy számot: "))
szam_3 = float(szam_1)
szam_2 = int(input("Kérek egy másik számot: "))
osszeg = szam_1 + szam_2
print(f"A két szám összege: {osszeg}")
print(f"A megadott két szám összege: {szam_1 + szam_2}")
print(f"A szam_1 változó típusa: {type(szam_1)}")
print(f"szam_3változó típusa: {type(szam_3)}")
print(f"A szam_2 változó típusa: {type(szam_2)}")
print(f"A osszeg változó típusa: {type(osszeg)}")