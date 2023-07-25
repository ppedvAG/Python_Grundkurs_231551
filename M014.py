# Datenbankverbindung

# Hierfür wird sqlite3 verwendet

import sqlite3 as sql

def dbTest():
	# Verbindung zur Datenbank herstellen, wird neu erstellt falls nicht existent
	connection = sql.connect("Test.db")

	# Cursor: Komponente die SQL-Statements empfängt und weiterleitet
	cursor = connection.cursor()

	cursor.execute("create table test (id int, name varchar(50))")

	cursor.execute("insert into test values (1, 'Lukas')")
	connection.commit()  # Insert an die Datenbank schicken

	print(cursor.execute("select * from test").fetchall())

try:
	with sql.connect("Test.db") as conn:  # Bei SQL-Connections sollte mit with gearbeitet werden
		cursor = conn.cursor()
		cursor.execute("create table if not exists test (id int, name varchar(50))")
		id = int(input("Gib eine ID ein: "))
		name = input("Gib deinen Namen ein: ")
		cursor.execute(f"insert into test values ({id}, '{name}')")
		conn.commit()
		print(cursor.execute("select * from test").fetchall())
except sql.Error:
	print("SQL Error")

# Übung
# Erstelle ein Programm, das beim Ausführen eine neue Datenbank 'Lab.db' anlegt, falls sie noch nicht existiert
# Das Programm soll beim Start auch die Tabelle Users mit der Spalte name erstellen
# Ermögliche dem User folgende Funktionen:
#    - Er soll neue Benutzer erstellen können (Er soll den Benutzernamen angeben und dieser soll dann in die Tabelle eingefügt werden)
#    - Er soll nach Benutzern suchen können (Die Funktion soll als Parameter den Namen des Useres akzeptieren und das Programm soll alle Ergebnisse in die Konsole ausgeben)
#    - Er soll die Möglichkeit haben Benutzer zu löschen (Er soll den Benutzernamen angeben der gelöscht werden soll)
