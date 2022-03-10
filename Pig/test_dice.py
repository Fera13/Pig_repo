import unittest
from dice import Dice


ic = Dice()


class testDice(unittest.TestCase):
    def test_roll_TypeError(self):
        '''Testing for type error'''
        with self.assertRaises(TypeError):
            ic.roll("2")
        with self.assertRaises(TypeError):
            ic.roll(2.2)

    def test_roll_ValueError(self):
        '''Testing for value error'''
        with self.assertRaises(ValueError):
            ic.roll(-2)
        with self.assertRaises(ValueError):
            ic.roll(-10)
        with self.assertRaises(ValueError):
            ic.roll(0)

    def test_hardAiRoll_TypeError(self):
        '''Testing for type error'''
        with self.assertRaises(TypeError):
            ic.hardAiRoll("2")
        with self.assertRaises(TypeError):
            ic.hardAiRoll(2.2)

    def test_hardAiRoll_ValueError(self):
        '''Testing for value error'''
        with self.assertRaises(ValueError):
            ic.hardAiRoll(0)
        with self.assertRaises(ValueError):
            ic.hardAiRoll(-2)

    def test_easyAiRoll_TypeError(self):
        '''Testing for type error'''
        with self.assertRaises(TypeError):
            ic.easyAiRoll("2")
        with self.assertRaises(TypeError):
            ic.easyAiRoll(2.2)

    def test_easyAiRoll_ValueError(self):
        '''Testing for value error'''
        with self.assertRaises(ValueError):
            ic.easyAiRoll(0)
        with self.assertRaises(ValueError):
            ic.easyAiRoll(-2)

    def test_resetTotal_returnValue(self):
        '''Testing that the total scores get reset'''
        self.assertEqual(ic.resetTotals(), 0)

    def test_cheatDice_returnValue(self):
        '''Testing that the return value is 99 and the cheat\
            has been activated'''
        self.assertEqual(ic.cheatDice(), 99)


if __name__ == "__main__":
    unittest.main()
