"""
This tets the game functionality class.

Authors: Farah, Alfred, Emil
"""
import unittest
from game_functionality import GameFunctionality

gf = GameFunctionality()


class TestGameFunctionality(unittest.TestCase):
    """Tests the game functionality class."""

    def test_handle_menu_choice_wrong_value(self):
        """Tests that an error will be raised if the wrong type of arguments\
             is entered."""
        with self.assertRaises(ValueError):
            gf.handle_menu_choice("hi")


if __name__ == "__main__":
    unittest.main()
