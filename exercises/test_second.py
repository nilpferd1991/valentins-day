from unittest import TestCase
from greatest import greatest

# Schreibe eine Function greatest, welche die Zahl aus second.dat ausliest und die 13 aufeinanderfolgenden
# Zahlen liefert, welche das größte Produkt besitzen.
class TestSecond(TestCase):
    def test_greatest(self):
        self.assertEqual(greatest(), 1)
