# studienkolleg
Unterrichtsmaterialien für den Informatikunterricht am Studienkolleg der TU Berlin

[Alle PDF-Dateien herunterladen](https://github.com/kinnla/studienkolleg/releases/download/pdfs-latest/compiled-pdfs.zip)

## LaTeX-Konventionen

Bei jedem Push werden alle `.tex`-Dateien automatisch zu PDFs compiliert.

**Dateien mit führendem `_` werden nicht compiliert.** Sie dienen als Fragment-Dateien (z.B. `_body.tex`) die per `\input` von einer Hauptdatei eingebunden werden. Die Hauptdatei definiert dabei den Kontext (Preamble, Makros), das Fragment enthält nur den Inhalt.

Beispiel für Aufgabenblätter mit Musterlösung:
- `aufgabe.tex` — compiliert zu `aufgabe.pdf` (nur Aufgaben)
- `aufgabe_loesungen.tex` — compiliert zu `aufgabe_loesungen.pdf` (Aufgaben + Lösungen in grünen Kästen)
- `_aufgabe_body.tex` — Fragment mit Aufgaben und `\loesung{...}`-Blöcken, wird nicht direkt compiliert
