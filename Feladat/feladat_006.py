"""
gondolt_szám = 4
ki: "gondoltam egy számra"
be: tipp
tipp átalakítása egésszé
elágazás
ha tipp = gondolt szám:
ki: dicséret
elágazás vége
ki: búcsú
"""

gondolt_szám = 4
tipp = input ('Gondoltam egy számra. Tippeld meg!')
tipp = int(tipp)
if tipp == gondolt_szám:
    print(f'Ügyes vagy!')
print('Pápá!')    