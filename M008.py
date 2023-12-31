import json
import xml

# Input/Output

# print(...)
# input(string)
# Konsoleneingabe mit Text (Prompt)
# Warte auf den Input vom User (Programm bleibt stehen)

# name = input("Gib deinen Namen ein: ")
# print(f"Dein Name ist {name}")
#
# zahl = int(input("Gib eine Zahl ein: "))
# print(zahl)

# Escape-Sequenzen:
# \n, \r: Zeilenumbruch, \t: Tabulator, \" \' \\
print("Das ist \n\t ein\"\'\\ Umbruch")

# open(Pfad, Modus)
file = open("Test.txt", "w")
file.writelines("Test1")  # Text in die Datei schreiben

# Wenn ein Stream geöffnet wird, muss dieser auch geschlossen werden
# Generell wird ein Stream geschlossen am Ende des Skripts
# Solange der Stream offen ist, kann das File nicht bearbeitet/gelöscht werden
file.close()

allText: list[str]
with open("Test.txt", "r") as readFile:
	allText = readFile.readlines()

# Json
# Werden verwendet, um Objekte zwischen Programmen hin und her zu bewegen
# z.B.: Webschnittstelle
testList = (1, 2, 3)

jsonStr = json.dumps(testList)  # dump-string -> Konvertiert ein Objekt zu einem Json String
print(jsonStr)
# json.dump(...): Schreibt das Json direkt in ein File

readJsonList = json.loads(jsonStr)  # load-string -> Konvertiert den Json String in ein Objekt
print(type(readJsonList))
# json.load(...): Liest ein File ein und konvertiert es

# rstring
# String, der keine Escape-Sequenzen interpretiert
pfad = "C:\\Users\\lk3\\source\\repos\\Python_Grundkurs_2023_07_20"
pfadR = r"C:\Users\lk3\source\repos\Python_Grundkurs_2023_07_20"

# Überprüfen ob eine Datei existiert
import os
if os.path.exists("Name"):
	print("Existiert")

# Übung 1:
# Funktion die dem User die Möglichkeiten (w, r, a) gibt
# User soll eine davon auswählen über input()
# Wenn der User keine valide Möglichkeit eingibt, soll die Eingabe wiederholt werden
# Danach soll einfach das File geöffnet werden
# Bonus: Frage den Benutzer nach dem File, welches geöffnet werden soll
def auswahl():
	while True:  # Endlosschleife bis der User etwas korrektes eingibt
		# if choice == "w" or choice == "r" or choice == "a":
		choice = input("Gib w, r oder a ein: ")
		if choice in ["w", "r", "a"]:  # in statt if/or
			break
	print("Valide Eingabe, File wird geöffnet")
	return open("Test.txt", choice)

# Übung 2:
# Erstelle ein Programm, das zwei Integer oder Floats abfragt
# Gib dem Nutzer die Möglichkeit per Tastendruck zwischen Addition, Subtraktion, Multiplikation und Division zu wählen.
# -> Zahl zwischen 1 und 4 -> Rechenoperation auswählen
# Bei Ungültiger Eingabe soll der Benutzer erneut nach seiner Entscheidung gefragt werden.
# Lasse das Ergebnis inklusive der Berechnung in der Konsole ausgeben
# Frage nach Ende der Operation ob der Benutzer eine neue Berechnung durchführen will
def rechner():
	while True:
		while True:
			zahl1 = input("Gib die erste Zahl ein: ")
			if zahl1.isnumeric():
				zahl1 = int(zahl1)
				break

		while True:
			zahl2 = input("Gib die zweite Zahl ein: ")
			if zahl2.isnumeric():
				zahl2 = int(zahl2)
				break

		while True:
			operation = input("Gib eine Rechenoperation ein (+, -, *, /): ")
			if operation in ["+", "-", "*", "/"]:
				break

		if operation == "+":
			print(f"{zahl1} + {zahl2} = {zahl1 + zahl2}")
		if operation == "-":
			print(f"{zahl1} - {zahl2} = {zahl1 - zahl2}")
		if operation == "*":
			print(f"{zahl1} * {zahl2} = {zahl1 * zahl2}")
		if operation == "/":
			print(f"{zahl1} / {zahl2} = {zahl1 / zahl2}")

		wiederholung = input("Wiederholen? (Y)")
		if wiederholung != "Y":
			break

if __name__ == "__main__":
	rechner()