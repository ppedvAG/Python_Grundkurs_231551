# Vererbung
# Klassen können eine Oberklasse haben, und damit eine Vererbungshierarchie herstellen
# z.B.:
# Lebewesen ->
# --- Mensch
# --- Katze
# --- Hund
# --- ...
# Oberklassen geben ihre Funktionen & Variablen nach unten weiter

class Lebewesen:
	def __init__(self, name: str = ""):
		self.name = name

	# Der Typ von self passt sich automatisch auf die Instanz an
	def bewegen(self, distanz: int):
		"""
		Mithilfe dieser Funktion kann das Lebewesen sich um eine bestimmte Distanz in Meter bewegen.

		:param distanz: Die Distanz in Meter
		"""
		print(f"{type(self).__name__} hat sich um {distanz}m bewegt")

	def __str__(self):
		"""
		Gibt eine String Repräsentation des Objekts zurück.

		:return: Einen String.
		"""
		return f"Mein Name ist {self.name}"


class Mensch(Lebewesen):
	"""
	Das ist die Mensch Klasse. Sie erbt von Lebewesen, implementiert selbst die Sprechen Funktion und die Alter Variable.
	"""
	# Mensch erbt bewegen, name, __init__

	def __init__(self, name: str, alter: int):
		self.alter = alter
		super().__init__(name)  # super(): Code der Oberklasse verwenden (Funktionen verketten)

	def __str__(self):
		return f"{super().__str__()} und ich bin {self.alter} Jahre alt"  # Wenn oben in __str__() etwas geändert wird, passt es sich hier automatisch an

	def sprechen(self, nachricht: str):
		print(nachricht)


mensch = Mensch("Max", 30)
mensch.bewegen(10)  # Mensch hat bewegen von Lebewesen geerbt
mensch.name = "Max"  # Mensch hat name von Lebewesen geerbt
print(mensch)

# docstring
# Wird geschrieben mit """ ... """ (auch mit ''' möglich)
# Enthält Beschreibungen zum Code (Dokumentation)
# Muss unter dem Typen definiert werden
# Mit :param <Name>: und :return: können die entsprechenden Dinge Dokumentiert werden