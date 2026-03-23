# debug4.py - Finden und beheben Sie den Fehler!
# Das Programm soll einen Countdown ausgeben und dann die Summe aller Zahlen.

n = int(input("Countdown ab welcher Zahl? "))

while n > 0:
    print(n)
    summe = summe + n
    n = n - 1

print("Start!")
print(f"Die Summe aller Zahlen ist {summe}.")