import unittest
from dice import *


ic = Dice()


class testDice(unittest.TestCase):
    def test_roll_TypeError(self):
        with self.assertRaises(TypeError): Dice.roll("2")
        with self.assertRaises(TypeError): Dice.roll(2.2)


    def test_roll_ValueError(self):
        with self.assertRaises(ValueError): ic.roll(-2)
        with self.assertRaises(ValueError): ic.roll(-10)
        with self.assertRaises(ValueError): ic.roll(0)


    def test_hardAiRoll_TypeError(self):
        with self.assertRaises(TypeError): ic.hardAiRoll("2")
        with self.assertRaises(TypeError): ic.hardAiRoll(2.2)
    

    def test_hardAiRoll_ValueError(self):
        with self.assertRaises(ValueError): ic.hardAiRoll(0)
        with self.assertRaises(ValueError): ic.hardAiRoll(-2)


    def test_easyAiRoll_TypeError(self):
        with self.assertRaises(TypeError): ic.easyAiRoll("2")
        with self.assertRaises(TypeError): ic.easyAiRoll(2.2)
    

    def test_easyAiRoll_ValueError(self):
        with self.assertRaises(ValueError): ic.easyAiRoll(0)
        with self.assertRaises(ValueError): ic.easyAiRoll(-2)


    def test_resetTotal_returnValue(self):
        self.assertEqual(ic.resetTotals(), 0)


    def test_cheatDice_returnValue(self):
        self.assertEqual(ic.cheatDice(), 99)


if __name__ == "__main__":
    unittest.main()
