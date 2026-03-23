# debug2.py - Finden und beheben Sie den Fehler!
# Das Programm soll die Summe aller Zahlen von 1 bis n berechnen.

n = input("Bis zu welcher Zahl soll summiert werden? ")

summe = 0
for i in range(1, n + 1):
    summe = summe + i

print(f"Die Summe von 1 bis {n} ist {summe}.")
