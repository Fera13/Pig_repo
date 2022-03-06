import unittest
from dice import *

ic = dice()

class testDice(unittest.TestCase):
    def test_roll_wrongType(self):
        with self.assertRaises(TypeError): dice.roll(2)
        self.assertEqual(ic.testmethod(3), 2)


if __name__ == "__main__":
    unittest.main()