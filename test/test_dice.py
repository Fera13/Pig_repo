"""
This tests the dice class.

Authors: Farah, Alfred, Emil
"""
import unittest
from dice import Dice


ic = Dice()


class TestDice(unittest.TestCase):
    """Test the dice class."""

    def test_roll_type_error(self):
        """Testing for type error."""
        with self.assertRaises(TypeError):
            ic.roll("2")
        with self.assertRaises(TypeError):
            ic.roll(2.2)

    def test_roll_value_error(self):
        """Testing for value error."""
        with self.assertRaises(ValueError):
            ic.roll(-2)
        with self.assertRaises(ValueError):
            ic.roll(-10)
        with self.assertRaises(ValueError):
            ic.roll(0)

    def test_hard_ai_roll_type_error(self):
        """Testing for type error."""
        with self.assertRaises(TypeError):
            ic.hard_ai_roll("2")
        with self.assertRaises(TypeError):
            ic.hard_ai_roll(2.2)

    def test_hard_ai_roll_value_error(self):
        """Testing for value error."""
        with self.assertRaises(ValueError):
            ic.hard_ai_roll(0)
        with self.assertRaises(ValueError):
            ic.hard_ai_roll(-2)

    def test_easy_ai_roll_type_error(self):
        """Testing for type error."""
        with self.assertRaises(TypeError):
            ic.easy_ai_roll("2")
        with self.assertRaises(TypeError):
            ic.easy_ai_roll(2.2)

    def test_easy_ai_roll_value_error(self):
        """Testing for value error."""
        with self.assertRaises(ValueError):
            ic.easy_ai_roll(0)
        with self.assertRaises(ValueError):
            ic.easy_ai_roll(-2)

    def test_reset_total_return_value(self):
        """Testing that the total scores get reset."""
        self.assertEqual(ic.reset_totals(), 0)

    def test_cheat_dice_return_value(self):
        """Testing that the return value is 99 and the cheat\
            has been activated."""
        self.assertEqual(ic.cheat_dice(), 99)


if __name__ == "__main__":
    unittest.main()