# Decorator
# Sind Funktionen, die andere Funktionen anpassen
# Werden mit @<Name> hinzugefügt
import time


# Auch Funktionen sind Objekte
def test():
	pass

print(test)  # <function test at 0x00000270064A3E20>

func = test
print(func)  # <function test at 0x00000270064A3E20>

# Eigenen Decorator, kann später an Funktionen mit @testDecorator angehängt werden
def testDecorator(function):
	def wrapper():
		print("Vor der Funktion")
		function()  # Function Parameter aufrufen
		print("Nach der Funktion")

	return wrapper  # Funktionszeiger (die fertig dekorierte Funktion) zurückgeben

def hello():
	print("Hello World")

decoratedHello = testDecorator(hello)  # Hier lasse ich hello() dekorieren
decoratedHello()

@testDecorator
def bye():
	print("Bye World")

bye()

# Decorator mit Parametern
def testDecoratorParam(function):
	def wrapper(*args, **kwargs):  # Decorator Parameter mit * und ** Parametern um alle möglichen Parameter abzudecken + Anzahl
		print("Vor der Funktion")
		return function(*args, **kwargs)  # Das Ergebnis der übergebenen Funktion zurückgeben

	return wrapper


@testDecoratorParam
def add(z1, z2):
	return z1 + z2

print(add(6, 7))


def measureTime(func):
	def wrapper(*args, **kwargs):
		startTime = time.time()
		func(*args, **kwargs)
		print(f"Benötigte Zeit: {float(int((time.time() - startTime)*100))/100} Sekunden")

	return wrapper


@measureTime
def print100_000():
	for i in range(100_000):
		print(i)

# print100_000()


class Square:
	def __init__(self, seitenlaenge: int):
		self._seitenlaenge = seitenlaenge  # private Variable, ist in Python nur eine Empfehlung

	@property
	def seitenlaenge(self):
		print("Seitenlänge wurde angegriffen")
		return self._seitenlaenge

	@seitenlaenge.setter
	def seitenlaenge(self, neueLaenge):
		if neueLaenge > 0 and neueLaenge < 100:
			self._seitenlaenge = neueLaenge
		else:
			print("Neue Länge zu klein/groß")

square = Square(10)
print(square._seitenlaenge)  # Sollte nicht angegriffen werden
print(square.seitenlaenge)
square.seitenlaenge = 20