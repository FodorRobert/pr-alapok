#feladat_015
"""
Kérjük be a vezeték és keresztnevünket
Írassuk ki függvény segítségével nevünket.
"""

vezetek = input("Kérem a vezetékneved: ")
kereszt = input("Kérem a keresztned: ")

def nevf(vnev, knev):    
    nevem = vnev + ' ' + knev
    return nevem

print(f"A nevem: {nevf(vezetek, kereszt)}")