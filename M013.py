# Fehlerbehandlung

def doStuff(test):
	print(test)

# doStuff()  # TypeError (ein fehlendes Argument)

# xyz()  # NameError (Member existiert nicht)

def rec():
	rec()

# rec()  # RecursionError (Zu viel Rekursion)

# eingabe = int(input("Gib eine Zahl ein: "))  # ValueError (keine Zahl eingegeben)

try:
	eingabe = int(input("Gib eine Zahl ein: "))  # ValueError falls der Benutzer keine Zahl eingibt
	print(5 / eingabe)
except ValueError as e:  # Nur ValueError fangen (Except Blöcke werden sequentiell abgearbeitet)
	print("Keine Zahl eingegeben")
	print(e)  # Standardnachricht des Fehlers ausgeben
except ZeroDivisionError:
	print("Division durch 0 nicht möglich")
except Exception as e:  # Alle anderen Fehler abfangen
	print("Anderer Fehler")
else:  # Wird ausgeführt, wenn kein Fehler aufgetreten ist
	print("Kein Fehler")
finally:  # Wird immer ausgeführt, auch bei Fehlern
	print("Immer ausgeführt")

print("Nach dem try/except Block")

if eingabe < 5:
	raise OSError("Eine Nachricht")  # raise: Fehler verursachen/Exception werfen

# Eigene Exception definieren
class CoffeeError(Exception):
	def __init__(self, msg="", status=""):
		super().__init__(msg)
		self.status = status

try:
	if eingabe >= 10:
		raise CoffeeError("Ein Fehler", "Fehler")
except CoffeeError as e:  # Eigene Daten durch Exceptions bewegen
	print(e.status)

# Übung 1
# Erstelle ein Programm, das den User nach zwei Integern fragt
# Falls der User zwei Integer eingibt sollen diese addiert und das Ergebnis in der Konsole ausgegeben werden und das Programm kann beendet werden
# Falls der Benutzer einen falschen Typen eingibt soll das Programm ihn darauf hinweisen, dass nur Integer akzeptiert werden und ihn erneut nach den Zahlen fragen

# Übung 2
# Definiere eine beliebige Liste
# Erstelle ein Programm, das es den User fragt, das wievielte Element in der Konsole ausgegeben werden soll
# Falls die Zahl außerhalb des Listen-Indexes liegt soll ein Fehler geworfen und der User darauf hingewiesen werden

# Übung 3
# Füge der beschleunigen Funktion deiner Fahrzeug-Klasse aus Modul 9 eine eigene Exception hinzu:
#    - Sie soll geworfen werden, falls die Höchstgeschwindigkeit überschritten wird
