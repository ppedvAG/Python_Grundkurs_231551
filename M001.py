# Ich bin ein Kommentar
# Keine Mehrzeiligen Kommentare

x = 5  # Variablen nehmen den Typ des Inhalts an -> int
x = "Test"  # x ändert ihren Typen auf str

# Datentypen
# int, float, str, bool

# Integer, kann beliebig große/kleine Zahlen halten
zahl = 48756923754982436019736548372973428593475897

# Float, kann beliebig große/kleine Zahlen halten
kommazahl = 3875913287492078592308.293759025789234080

# str (String), auch verantwortlich für einzelne Zeichen (char)
zeichen = "A"
test = 'Text'  # Einzelne Hochkomma sind identisch zu doppelten Hochkomma (Konvention gibt einzelne Hochkomma vor)

# bool, True oder False
wahr = True
falsch = False

# Stringfunktionen
text = "Max Mustermann"

# str.count("Zeichen"): Zählt die Anzahl der Vorkommnisse des Zeichens
text.count("M")
print(text.count("M"))

# str.lower(), str.upper(): Macht den gesamten String lowercase oder UPPERCASE
print(text.lower())
print(text.upper())

# Lower und Count kombinieren für eine Case-Insensitive Suche
print(text.lower().count("m"))

# str.islower(), str.isupper(): Schaut ob der gesamte String lowercase oder UPPERCASE ist
print(text.islower())
print(text.isupper())

# Index (eckige Klammern)
# Wird verwendet, um eine Collection an einer Stelle anzugreifen
# Verwendung: variable[<Index>]
print(text[0])  # M
print(text[0].isupper())  # True

# type(<Variable>): Gibt den Typen der Variable aus
print(type(text[0]))

# len(<Variable>)
# Gibt die Länge es iterierbaren Objekts aus
print(len(text))

# Mit dem Index kann auch von rechts auf das Objekt gegriffen werden oder ein Bereich genommen werden
print(text[-1])  # Das letzte Zeichen (der Rechtsbasierte Index ist 1-basiert)
print(text[0:3])  # Nimm alle von Zeichen von 0 bis 2 (Obergrenze exkludiert)
print(text[-4:-1])  # Von rechts 4 Zeichen nach links, -1 exkludiert
print(text[4:])  # Von Zeichen 4 bis zum Ende
print(text[-4:])  # Von rechts
print(text[:3])  # Vom ersten Zeichen bis zu 2

# str.isalpha(), str.isnumeric(), str.isalnum()
print(text.isalpha())  # Nur Zeichen
print(text.isnumeric())  # Nur Ziffern
print(text.isalnum())  # Nur Zeichen und Ziffern

# complex
# Komplexe Zahlen
complex = 5 + 12j

# Arithmetische Operatoren
# +, -, *, /
# Modulo %
# Potenzieren **
# Ganzzahldivision //
zahl1 = 5
zahl2 = 8

print(zahl1 + zahl2)  # Verändert nicht die originalen Zahlen
zahl1 += zahl2  # Hier wird zahl2 auf zahl1 draufaddiert

print(zahl1 % zahl2)
print(zahl1 ** zahl2)
print(zahl1 // zahl2)

# Arithmetik mit Strings
wort1 = "Ein"
wort2 = "Wort"
print(wort1 + wort2)
wort1 += wort2

# String multiplizieren
print(wort1 * 20)  # EinWortEinWortEinWortEinWortEinWortEinWortEinWortEinWortEinWortEinWortEinWortEinWortEinWortEinWortEinWortEinWortEinWortEinWortEinWortEinWort
wort1 *= 5

# Übung1
# Lege drei numerische Variablen an, addiere sie zusammen und schreibe das Ergebnis in eine neue Variable
# Potenziere danach die Variable mit sich selbst und schreibe das Ergebnis erneut in eine Variable

# Übung2
# Nimm die potenzierte Zahl aus Übung1 und stelle fest ob diese Restlos durch 2 teilbar (gerade) ist

# Übung3
# Lege zwei Variablen an: Vorname befüllt mit Max und Nachname befüllt mit Mustermann
# Verbinde diese zwei Variablen und zähle danach die Buchstaben 'M' und 'm'
# Das Ergebnis soll 3 sein

# Übung4
# Schreibe deinen Vornamen ohne Großbuchstaben in eine Variable
# Verwende danach diese Variable, und gib diese mit dem ersten Buchstaben groß geschrieben aus
