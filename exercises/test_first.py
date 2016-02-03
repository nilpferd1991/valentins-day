from unittest import TestCase

from prim import prim

# Erste Aufgabe: Schreibe eine Funktion prim(n), 
# welche alle Primzahlen kleinergleich als n zurückgibt.
class TestFirst(TestCase):
    def test_one(self):
        self.assertEqual(prim(2), [2])
    
    def test_two(self):
        self.assertEqual(prim(10), [2, 3, 5, 7])

    def test_three(self):
        self.assertEqual(prim(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

