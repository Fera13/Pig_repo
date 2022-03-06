import unittest
from dice import *

class testDice(unittest.TestCase):
    def test_roll_wrongType(self):
        with self.assertRaises(TypeError): Dice.roll("2")


if __name__ == "__main__":
    unittest.main()