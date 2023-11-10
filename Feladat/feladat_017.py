#feladat_017
#Adatbekérés while ciklussal

# while szam < 5 or 10 < szam:
szam = int(input("Kérlek adj meg egy számot 5 és 10 között! "))
while not 5 <= szam <= 10:
    szam = int(input('Helytelen érték! Adj meg egy számot 5,6,7,8,9,10! '))

print('Rendben!')