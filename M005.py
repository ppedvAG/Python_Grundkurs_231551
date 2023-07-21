# List Comprehension
# Gibt die Möglichkeit anhand eines Ausdrucks eine Liste zu erzeugen

# Normal (ohne LC)
zahlenBis100 = list()
for i in range(100):
	zahlenBis100.append(i)

zahlenBis100LC = [i for i in range(100)]  # Normale Schleife, Variablenname davor (kann bearbeitet werden)
print(zahlenBis100LC)

zahlenIHochI = [i ** i for i in range(20)]  # i^i bis 20 in einer Liste
print(zahlenIHochI)

zahlenIHochIOhne14 = [i ** i for i in range(20) if i != 14]  # Mit Bedingungen die LC nochmals einschränken
print(zahlenIHochIOhne14)

# Verschachtelte Schleifen
kleines1x1 = [f"{z1} * {z2} = {z1 * z2}" for z1 in range(1, 11) for z2 in range(1, 11)]  # Kleines 1x1 mit LC
for element in kleines1x1:
	print(element)

print([f"{i}: Teilbar durch 3" if i % 3 == 0 else f"{i}: Nicht teilbar" for i in range(1, 100)])  # Ternary Operator in LC

wortListe = ["Das", "iSt", "einE", "LisTe"]

print([w for w in wortListe if w[0].isupper()])  # Nur großgeschriebene Wörter

print([w.capitalize() if w[0].isupper() else w.lower() for w in wortListe])  # Fehler beheben

print([w for w in wortListe if "e" in w.lower()])  # Nur Wörter mit einem E drin (Case Insensitive)

# Übung 1
# Schreibe eine List-Comprehension die nur Zahlen aus einer Range von 1 bis inklusive 30 in die neue Liste packt,
# falls die Zahl durch 6 teilbar ist
# Bevor die Zahl in die neue Liste gepackt wird, soll sie um 12 erhöht werden
print([num + 12 for num in range(1, 31) if num % 6 == 0])

# Übung 2
# Schreibe eine List-Comprehension die aus einem Text alle Kleinbuchstaben nimmt und Groß in die Liste schreibt
text = "Ich bin ein Text"
print([b.upper() for b in text if b.islower()])

# Übung 3
# Schreibe eine List-Comprehension die aus einem Text alle Anfangsbuchstaben nimmt
print([wort[0] for wort in text.split(" ")])
print([wort[0] for wort in text.title() if wort.isupper()])

# Übung 4
# Schreibe eine List-Comprehension die aus einem Text alle Wörter nimmt die 3 oder weniger Zeichen haben
print([wort for wort in text.split(" ") if len(wort) <= 3])


# match-case
# = Switch
a = 10
match a:
	case 5:
		print("Die Zahl ist 5")
	case 6:
		print("Die Zahl ist 6")
	case 7, 8:  # Cases kombinieren
		print("Die Zahl ist 7 oder 8")
	case _ if a < 10:  # Case mit Bedingung
		print()
	case _:
		print("Default")