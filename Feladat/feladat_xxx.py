#feladat_014
"""
Kérjük be a vezeték és keresztnevünket
Írassuk ki eljárás segítségével nevünket.
"""

vezetek = input("Kérem a vezetékneved: ")
kereszt = input("Kérem a keresztned: ")

def nev(vnev, knev):    
    print(f"A nevem: {vnev} {knev}.")

nev(vezetek, kereszt)