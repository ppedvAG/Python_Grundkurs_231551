# Klassen und Objekte

# Objekt
# Alles in Python sind Objekte (Variablen, Funktionen, Klasse)
# Jedes Objekt hat einen Typen (int, str, bool, float, list, tuple, ...)
# Jedes Objekt hat alle Variablen und Funktionen die in der Klasse hinter dem Objekt vorgegeben wurden
i = 12
i.as_integer_ratio()  # Variable hat die Funktionen der Klasse
print(type(i))  # <class 'int'>

# isinstance(Variable, Typ): Überprüft, ob eine Variable einen bestimmten Typen hat
print(isinstance(i, int))
print(isinstance(i, str))

# Genauer Typvergleich
if type(i) == object:
	print("i ist object (type)")

# Vererbungshierarchie Typvergleich
if isinstance(i, object):
	print("i ist object (is)")

# Klasse
# Bauplan, aus dem Objekte erstellt

class Tisch:
	x = "Test"  # Klassenvariable, ist auf der Klassenebene sichtbar (global) und wird geteilt zwischen allen Objekten der Klasse

	# Konstruktor
	# Wird aufgerufen, wenn das Objekt erstellt wird
	# Hier müssen Instanzvariablen angelegt werden
	# Bei Konstruktoren können auch extra Parameter hinzugefügt werden
	# Es kann nur einen Konstruktor geben, mehrere Konstruktoren müssen über optionale Parameter "deklariert" werden
	def __init__(self, y=0):
		print("Ein Tisch wurde erstellt")
		self.y = y  # Instanzvariable, ist von Instanz zu Instanz unabhängig -> hat verschiedene Werte pro Objekt

	def move(self, x: int, y: int):
		print(f"Der Tisch hat sich um {x + y}m bewegt")

	def __str__(self):
		return f"Das ist ein Tisch und er hat den Wert {self.y} für y"

# pass  # Mach nix, Platzhalter für einen leeren Codeblock

tisch = Tisch()  # Tisch erstellen
tisch.move(4, 5)  # Funktion von dem Objekt benutzen
tisch.y = 10

print(type(tisch))  # <class '__main__.Tisch'>

# In Python können Instanzen (Objekte) neue Variablen erhalten
# <Variablenname>.<Neuer Name> = <Wert>
# Dynamic Properties sollten vermieden werden
tisch.z = 10
print(tisch.z)

del tisch.z
# print(tisch.z)  # Hier noch sichtbar, aber nicht existent

print(tisch)
# ohne __str__(): <__main__.Tisch object at 0x0000029956A8BFD0>
# mit __str__(): Das ist ein Tisch und er hat den Wert 10 für y

# Übung 1:
# 1. Erstelle eine Fahrzeug-Klasse
# 2. Diese Klasse soll typische Eigenschaften eines Fahrzeuges enthalten:
#     - Fahrzeug-Name
#     - Preis
#     - Maximale Geschwindigkeit
#     - Derzeitige Geschwindigkeit
#     - Motorzustand (An/Aus)
# 3. Die Klasse soll auch folgende Methoden enthalten:
#     - Beschleunigen (Erhöhe bzw Verringere die Derzeitige Geschwindigkeit aber übersteige nicht das Maximum) -> Parameter int (Wieviel soll beschleunigt werden)
#     - StarteMotor (Setze Motorzustand auf True, funktioniert nur wenn das Auto noch nicht gestartet ist)
#     - StoppeMotor (Motor kann nur gestoppt werden, wenn das Auto nicht fährt)
#     - Beschreibung (Gibt alle Informationen über die Klasse wieder)
# 4. Erstelle eine Instanz der Klasse und nutze die Beschreibungs Funktion (Konkrete Werte)
