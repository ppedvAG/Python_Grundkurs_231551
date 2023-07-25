# Unittesting

# Testet Teilbereiche des Programms
# Sollte regelmäßig ausgeführt werden um Fehler frühzeitig zu erkennen

import unittest
from unittest import TestCase
from M015b import addiere, subtrahiere, multipliziere, dividiere

class TestClass(TestCase):
	def testeAddiere(self):
		actual = addiere(5, 6)
		expected = 11
		self.assertEqual(expected, actual)

	def testeSubtrahiere(self):
		actual = subtrahiere(5, 6)
		expected = -1
		self.assertEqual(expected, actual, "Fehler")  # Eigene Fehlermeldung hinzufügen


if __name__ == '__main__':
	unittest.main()