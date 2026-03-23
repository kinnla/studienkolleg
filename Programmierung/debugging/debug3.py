# debug3.py - Finden und beheben Sie den Fehler!
# Das Programm soll prüfen, ob ein Buchstabe ein Vokal ist.

buchstabe = input("Geben Sie einen Buchstaben ein: ")
buchstabe = buchstabe.lower()

if buchstabe == "a" and buchstabe == "e" and buchstabe == "i" and buchstabe == "o" and buchstabe == "u":
    print(f"'{buchstabe}' ist ein Vokal.")
else:
    print(f"'{buchstabe}' ist kein Vokal.")
