# Funktionen

# Code wiederverwendbar machen
# Funktionen in Python sind Objekte und werden beim Ausführen des Skripts instanziert
# Wenn das Python in einem anderen Skript geladen wird (mittels import/from), wird es komplett ausgeführt
# def Statements werden dadurch ausgeführt, und somit werden alle Funktionen erstellt

def hallo():
	print("Hallo")


hallo()  # Funktion ausführen
hallo()  # Mehrmals ausführen


# Funktion mit Parameter
def hallo(deinName):
	print(f"Dein Name ist: {deinName}")


hallo("Lukas")
hallo(1)
hallo([1, 2, 3])


def halloGut(deinName: str):  # Mit : <Typ> den Benutzer auf einen Typen hinweisen
	if type(deinName) == str:
		print(deinName)


halloGut("Lukas")
halloGut(1)  # Warning, kein Fehler per sé
halloGut([1, 2, 3])  # Funktioniert


def addiere(x, y):  # x und y sollten numerische Werte sein
	return x + y


summe = addiere(4.5, 5.5)
print(summe)

print(addiere(4.5, 5.5))
print(addiere("4.5", "5.5"))


def addiereGut(x: int, y: int) -> int:  # Rückgabetyp festlegen mittels -> <Typ>, auch wieder nur eine Empfehlung
	return x + y


# Default Werte
# Der Benutzer kann den Standardwert eines Parametern überschreiben, muss aber nicht
def subtrahiere(x: int, y: int, z=0):
	return x - y - z


subtrahiere(4, 5, 6)  # 3 Parameter (z überschrieben)
subtrahiere(4, 5)  # 2 Parameter (z=0)


def addOrSub(x: int, y: int, sub=False):
	if ~sub:  # ~ ist gleich ! (not)
		print(x + y)
	else:
		print(x - y)


addOrSub(4, 5)
addOrSub(4, 5)
addOrSub(4, 5)
addOrSub(4, 5)
addOrSub(4, 5)
addOrSub(4, 5)
addOrSub(4, 5)
addOrSub(4, 5)
addOrSub(4, 5)
addOrSub(6, 2, True)  # Cornercase


def printPerson(vorname="", nachname="", alter=0, adresse=""):  # Methode mit 10+ Parametern
	print("...")

printPerson(alter=30, adresse="")  # Nur die Parameter befüllen die ich auch wirklich brauche
printPerson(vorname="", nachname="", adresse="")


# * Parameter (Arbitrary Arguments)
# Ermöglicht, beliebig viele Parameter einzugeben
def sumNumbers(*numbers: int):
	sum = 0
	for num in numbers:
		sum += num
	return sum

sumNumbers(1, 2, 3, 4, 5, 6, 7, 8)


def listTeilnehmer(**tn):
	for k, v in tn.items():
		print(f"Vorname {k}, Nachname {v}")

listTeilnehmer(T1="1", T2="2", T3="3")

# Unpacking Operatoren
# Ermöglichen, eine Liste von Einträgen in ihre Einzelteile zu zerlegen (für *args, **kwargs)
# * für Listen, ** für Dictionaries
sumNumbers(*[1, 2, 3, 4])
# sumNumbers(*"123456")
myDict = {
	"T1": 1,
	"T2": 2,
	"T3": 3
}
listTeilnehmer(**myDict)


# / Parameter
# Ermöglicht, die Reihenfolge von normalen Parametern zu erzwingen
def test(x, y, /, z, w):
	print()

# test(x=5, w=3, y=10, z=8)  # x und y müssen an der Korrekten Stelle sein
test(5, 3, w=3, z=6)

# Übung 1:
# Wir wollen eine Funktion erstellen, die beliebig viele Zahlen als Parameter erhalten kann
# Und uns die größte dieser Zahlen zurückgibt
# Auch negative Zahlen sollen berücksichtigt werden

# Übung 2:
# Wir wollen eine Funktion erstellen, die einen String als Paramter erhält
# Die Funktion soll dann in der Konsole ausgeben, aus wie vielen Klein- und Großbuchstaben der String besteht
# Die Funktion soll zusätzlich zählen wie viele Sonderzeichen (Nummern inkludiert) enthalten sind und das
# ebenfalls ausgeben
# Sonderzeichen: 4 | Groß: 3 | Klein: 12
