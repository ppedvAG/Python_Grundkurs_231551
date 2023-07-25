# Lambda Expessions

# Anonyme Funktionen: Funktionen die in einer Variable gespeichert und generell nur einmal verwendet werden
# In anderen Sprachen =>, ->
# Eigenschaften
# - Kein Name
# - Beliebig viele Parameter
# - Brauchen kein return bei Rückgabewerten
# - Darf nur eine Expression/Eine Zeile Code
# - Keine Schleifen, und kein break/continue

# Syntax:
# lamdba <Parameter>: <Body>
add = lambda x, y: x + y
summe = add(4, 5)
print(summe)

printAdd = lambda x, y: print(x + y)
printAdd(2, 3)

def addiere(x, y):
	return x + y


# Verwendung von Lambda-Expressions: Als Parameter für Funktionen
def lambdaTest(l):
	l()


# * und ** Argumente sind auch möglich
summiere = lambda *zahlen: sum(zahlen)

# Häufig verwendete Lambda-Funktionen
# filter(): Filtert die Liste anhand eines Kriteriums
# map(): Wandelt die Liste in eine neue Form um

# Die filter() Funktion
# Syntax:
# filter(<Lambda>, <Liste>)
# Filtert die Liste anhand der Lambda-Expression
# Lambda-Expression muss bool zurückgeben

zahlen = list(range(0, 10))

# Alle geraden Zahlen finden
neueZahlen = list()
for zahl in zahlen:
	if zahl % 2 == 0:
		neueZahlen.append(zahl)
print(neueZahlen)

# Mit List Comprehension
neueZahlenLC = [zahl for zahl in zahlen if zahl % 2 == 0]
print(neueZahlenLC)

# Mit Lambda
filterObjekt = filter(lambda zahl2: zahl2 % 2 == 0, zahlen)
print(list(filterObjekt))


def mod3(zahl):
	return zahl % 3 == 0

# Es können auch normale Funktionen als Funktionszeiger bei einer Lambda-Expression eingesetzt werden
print(list(filter(mod3, zahlen)))


# Die map() Funktion
# Syntax:
# map(<Lambda>, <Liste>)
# Wandelt die Liste in eine neue Form um

numberListMap = list(range(100))

listeMal2 = list()
for zahl in numberListMap:
	listeMal2.append(zahl * 2)
print(listeMal2)

# Mit LC
listeMal2LC = [zahl * 2 for zahl in numberListMap]
print(listeMal2LC)

# Mit Lambda
mapObjekt = map(lambda zahl: zahl * 2, numberListMap)
print(list(mapObjekt))

# Liste als String Repräsentation
print(list(map(lambda x: f"Die Zahl ist {x}", numberListMap)))

# Liste mit mehreren Spalten
print(list(map(lambda x: (x, x ** 2), numberListMap)))
print(list(map(lambda x: print((x, x ** 2)), numberListMap)))

list(map(lambda x: print(x), numberListMap))

# Übung 1
# Erstelle jeweils eine Lambda-Funktion die zwei Zahlen addiert bzw subtrahiert
# Führe diese Funktionen aus und gib die Ergebnisse in der Konsole aus

# Übung 2
# Nutze die filter() Funktion um eine Liste mithilfe von Lambdas nach folgenden Merkmalen zu filtern:
#    - Nur gerade Zahlen sollen in der neuen Liste enthalten sein
#    - Nur ungerade Zahlen sollen in der neuen Liste enthalten sein
#    - Nur Vielfache von 4 sollen enthalten sein

# Übung 3
# Nutze die map() Funktion um die Werte eine Liste mithilfe von Lambdas zu quadrieren
# Nutze die map(Funktion) um die Werte einer Liste zu halbieren