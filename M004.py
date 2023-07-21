# Schleifen

# for Schleife
# Verhält sich wie foreach in anderen Sprachen
# Braucht eine Collection (oder eine Range)

liste = ["Das", "ist", "eine", "Liste"]

for element in liste:
	print(element)
	print("Eine Zeile wurde geschrieben")  # Einrückungen beachten

for i in range(20):  # "Reguläre" for-Schleife
	print(i)

for i in range(0, len(liste)):  # "Reguläre" for-Schleife über eine Liste mit Index
	print(liste[i])

# break und continue
# break: Beendet die Schleife
# continue: Springt zum Schleifenkopf zurück
for i in range(10):
	print(i)
	if i == 5:
		break

for i in range(10):
	if i == 5:
		continue
	print(i)

# else bei Schleifen
# Führt ein Stück Code am Ende der Schleife aus
# Außer bei break oder bei Fehlern
for i in range(10):
	print(i)
else:
	print("Nach der Schleife")

# for Schleife über Dictionary
dictionary = {
	"Key1": "Value1",
	"Key2": "Value2",
	"Key3": "Value3"
}

for kv in dictionary.items():
	print(kv[0])
	print(kv[1])

for k in dictionary.keys():
	print(k)

for v in dictionary.values():
	print(v)

for k, v in dictionary.items():  # foreach Schleife mit 2 Schleifenvariablen
	print(k)
	print(v)

# while
# Läuft solange, wie die Bedingung True ist
while True:
	print("Endlos")
	break

x = 0
while True:
	x += 1
	if x == 500:
		break

# fstring, formatted String
# Code in einem String implementieren
# f"Der normale Text {<Code>}"
a = 5
fstring = f"Die Zahl ist {a}"
ohneFstring = "Die Zahl ist " + str(a)  # Mehr Aufwand

for i in range(0, 10):
	print(f"Die Zahl ist {i}")
	print(f"Die quadrierte Zahl ist {i * i}")
	print(f"{i} * {i} = {i * i}")

# Übung 1
# FizzBuzz
# 1. Schleife schreiben, die von 0 bis inklusive 100 hochzählt
# 2. Wir müssen in der Schleife jede Zahl auf ihre Teilbarkeit prüfen:
# Falls sie durch 3 teilbar ist, soll in der Konsole "Fizz" ausgegeben werden
# Falls sie durch 5 teilbar ist, soll in der Konsole "Buzz" ausgegeben werden
# Falls sie sowohl durch 3 als auch 5 teilbar ist, soll in der Konsole "FizzBuzz" ausgegeben werden
# Falls sie weder durch 3 noch 5 teilbar ist, soll die Zahl selbst in der Konsole ausgegeben werden
# 1
# 2
# Fizz
#  4
# Buzz
# ...
# 14
# FizzBuzz
for i in range(1, 100):
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	else:
		print(i)

# Übung 2
# Schreibe eine Schleife die dir alle Zahlen von 1 bis 200 zur Verfügung stellt
# Lass dir jede Zahl erst in der kardinalen und dann daneben in der ordinalen Schreibweise darstellen
# Zahl + Endung 'st', 'nd', 'rd' oder 'th'
# 1st, 2nd, 3rd, 4th, ..., 21st, 22nd, 23rd, 24th
# Bonus: Berücksichtige alle Zahlen die mit 11, 12 oder 13 enden
for i in range(1, 200):
	if i % 100 == 11 or i % 100 == 12 or i % 100 == 13:
		print(f"{i}: {i}th")
	elif i % 10 == 1:
		print(f"{i}: {i}st")
	elif i % 10 == 2:
		print(f"{i}: {i}nd")
	elif i % 10 == 3:
		print(f"{i}: {i}rd")
	else:
		print(f"{i}: {i}th")