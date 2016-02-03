from unittest import TestCase
from boston import boston

# Schreibe eine Function boston, welche das boston machine learning data sample herunterlädt (http://archive.ics.uci.edu/ml/datasets/Housing),
# ein pandas DataFrame mit sinnvollen Namen daraus generiert und die Anzahl an Häusern zurückgibt, welche am teuersten sind.
class TestThird(TestCase):
    def test_number(self):
        self.assertEqual(boston(), 16)
