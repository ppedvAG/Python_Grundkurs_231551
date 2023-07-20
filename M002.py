# List
# Typ der mehrere Werte halten kann
# Hat einen Index wie String
# Ist veränderbar
# Duplikate sind erlaubt
# Verschiedene Datentypen sind erlaubt, aber nicht empfohlen

meineListe = [1, 2, 3, 4, "Text", True]
print(meineListe)

# Index
print(meineListe[4])
print(meineListe[-1])
print(meineListe[1:4])

# list.append(): Fügt ein Element am Ende der Liste hinzu
meineListe.append(5)
print(meineListe)

# list.pop(<Index>): Entfernt ein Element am gegebenen Index
meineListe.pop(5)
print(meineListe)

# list.remove(<Wert>): Entfernt das erste Element das dem gegebenen Wert entspricht
meineListe.remove("Text")
print(meineListe)

# list.extend(<Liste>): Fügt alle Elemente aus der gegebenen Liste in meine Liste ein
meineListe.extend([1, 2, 3])
print(meineListe)

meineListe.sort()  # Sortiert die Liste
meineListe.clear()  # Entleert die Liste

# Tuple
# Verhalten sich ähnlich wie Listen
# Können allerdings nicht verändert werden
# Werden mit normalen Klammern ( ) deklariert
meinTuple = (1, 2, 3, 4)
print(meinTuple)

# Workaround um Tuple zu verändern
meinTuple = list(meinTuple)
meinTuple.append(5)
meinTuple = tuple(meinTuple)
print(meinTuple)

# Casting
# Konvertierung von einem Typ zu einem anderen Typen
zahl = "123"
zahlInt = int(zahl)
print(zahlInt * 2)

zahl2 = 123
zahlStr = str(zahl2)
print(zahlStr * 2)

# Ein String kann auch in eine Liste konvertiert werden
text = "Ein Text"
print(list(text))

# Unpacking
# Zerlegen von einer Collection in einzelne Variablen
unpacking = [1, 2, 3]
(eins, zwei, drei) = unpacking
print(eins)
print(zwei)
print(drei)

# Range
# Bereich von X bis Y
# Vorallem nützlich bei Schleifen
r100 = range(100)  # 0 bis Obergrenze - 1 -> 0-99
print(r100)  # range(0, 100) -> Range wurde noch nicht durchgegangen
print(list(r100))  # Iteration der Range erzwingen

print(list(range(-50, 50)))
print(tuple(range(-50, 51, 2)))  # Mit Schrittgröße

# Set
# Funktioniert wie Liste, ist aber eindeutig
# Benötigt die geschwungenen Klammern { }

meinSet = set()
meinSet.add(1)
meinSet.add(2)
meinSet.add(3)
meinSet.add(3)  # Wird nicht ausgeführt, da 3 bereits vorhanden
print(meinSet)

meineListe2 = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7]
print(set(meineListe2))  # Duplikate aus einer Liste entfernen

# Dictionary
# Liste von KeyValue Paaren
# Keys müssen eindeutig sein
meinCar = {
	"Brand": "Audi",
	"Model": "A3",
	"Year": 2017
}

print(meinCar)
print(meinCar["Year"])

meinCar["Year"] = 2020
meinCar["KM"] = 50000
print(meinCar)

# dict.keys(), dict.values(), dict.items()
# Keys, Values oder beides in Kombination holen
print(meinCar.keys())
print(meinCar.values())
print(meinCar.items())

# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]
# Kombiniere die drei Listen in eine ganze Liste und schließe Duplikate aus
list4 = list1 + list2 + list3
print(list(set(list4)))

# Übung 2
# Erstelle einen String und wandele ihn in eine Liste um, dabei soll jedes einzelne Zeichen ein Element der Liste werden
print(list("Ein Text"))

# Übung 3
# Lasse eine Liste erstellen die bei 0 beginnt und alle geraden Zahlen bis 20 enthält
# Nicht selbst schreiben, sondern Python machen lassen
print(list(range(0, 21, 2)))