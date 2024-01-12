Szélesség = float(input("Adja meg a téglalap szélességét: "))
Magasság = float(input("Adja meg a téglalap magasságát: "))
Terulet = Szélesség * Magasság

if Szélesség == Magasság:
    print("Ez egy négyzet.")

elif Szélesség < Magasság:
    print("Ez egy álló téglalap.")

elif Szélesség > Magasság:
    print("Ez egy fekvő téglalap.")

print(f"A területe {Terulet}.")