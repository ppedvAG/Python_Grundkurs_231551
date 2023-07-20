# Kontrollstrukturen

# Werden in Kombination mit logischen Operatoren verwendet

# Vergleichsoperatoren
# <, >, <=, >=
# ==, !=

# Logische Operatoren
# and, or, not
# in: Ist ein Element in einer Liste enthalten?
# is: Sind zwei Objekte identisch?

a = 4
b = 8
if a < b:  # Hier Doppelpunkt
	print("a kleiner b")  # Hier Einrückung

	if a > 5:
		print("a größer als 5")

	print("Außerhalb der inneren if")
print("Außerhalb beider ifs")

if a < b:
	print("a kleiner b")
elif a > b:  # Eigenes elif Keyword
	print("a größer b")
else:
	print("a gleich b")

print("a größer b" if a > b else "a kleiner-gleich b")

c = 10
if a < b and a < c or b < c:
	print("keine Ahnung")

if not a < b:
	print()

if 3 in [1, 2, 3, 4, 5]:
	print("3 ist in der Liste enthalten")

# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7]
# Finde heraus welche Liste die längste ist (es können auch mehrere Listen die längsten sein)
laengen = [len(list1), len(list2), len(list3)]
laengen.sort()
laengste = laengen[-1]
if len(list1) == laengste:
	print(list1)
if len(list2) == laengste:
	print(list2)
if len(list3) == laengste:
	print(list3)

# Übung 2
# Nimm die oberen drei Listen und überprüfe ob eine der Listen eine der drei Zahlen enthält: 3, 7, 10
kombi = list1 + list2 + list3
if 3 in kombi:
	print("3 enthalten")
if 7 in kombi:
	print("7 enthalten")
if 10 in kombi:
	print("10 enthalten")