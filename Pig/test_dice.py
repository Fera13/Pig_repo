import unittest
from dice import *

ic = dice()

class testDice(unittest.TestCase):
    def test_roll_wrongType(self):
        with self.assertRaises(TypeError): dice.roll("2")
        with self.assertRaises(TypeError): dice.roll(2.2)


    def test_roll_negativeValue(self):
        with self.assertRaises(ValueError): ic.roll(-2)
        with self.assertRaises(ValueError): ic.roll(-10)
        with self.assertRaises(ValueError): ic.roll(0)

if __name__ == "__main__":
    unittest.main()
