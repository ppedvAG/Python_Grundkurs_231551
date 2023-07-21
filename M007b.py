import sys
import M007

# Modul Suchpfade
# 1. Im selben Ordner wie das ausgeführte Skript
# 2. In der Standardbibliothek/venv
# 3. Ein bei der Installation konfigurierter zusätzlicher Pfad
# Wenn das Modul nicht gefunden wird -> ModuleNotFoundError
print(sys.path)
print(sys.version)
# sys.exit(0)  # Exit Code 0: Alles OK, Exit Code != 0: Fehler

# __name__: Gibt den Namen des Skripts zurück, oder __main__ falls das Skript direkt gestartet wurde
print(__name__)

# Pakete installieren
# 2 Möglichkeiten
# - Über Python Packages
# - Über pip (über Terminal/Powershell/Bash Shell)
# -- pip install <Paket>
# -- pip uninstall <Paket>

# __init__.py
# Beschreibt ein Init Skript
# Wird ausgeführt, wenn der entsprechende Ordner importiert wird

def main():
	print("Die Main Methode wurde ausgeführt")

# Diese Zeile wird ausgeführt, wenn das Skript direkt gestartet wird
# Wird in anderen Sprachen als Main Methode bezeichnet
# Generell am Ende eines Python Skripts zu finden
if __name__ == "__main__":
	main()