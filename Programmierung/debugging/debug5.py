# debug5.py - Finden und beheben Sie den Fehler!
# Die Funktion soll das Maximum einer Liste finden (ohne max() zu verwenden).

def finde_maximum(zahlen):
    groesste = zahlen[0]
    for zahl in zahlen:
        if zahl > groesste:
            groesste = zahl
            return groesste
    return groesste

werte = [3, 7, 2, 9, 4]
ergebnis = finde_maximum(werte)
print(f"Das Maximum von {werte} ist {ergebnis}.")
