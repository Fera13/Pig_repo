"""
This tets the game functionality class.

Authors: Farah, Alfred, Emil
"""
import unittest
from game_functionality import GameFunctionality

gf = GameFunctionality()


class TestGameFunctionality(unittest.TestCase):
    """Test the game functionality class."""

    def test_handle_menu_choice_wrong_value(self):
        """Test that an error will be raised if the wrong type of arguments \
is entered."""
        with self.assertRaises(ValueError):
            gf.handle_menu_choice("hi")

    def test_handle_menu_choice(self):
        """Test that everything is ok with the method."""
        self.assertEqual(gf.handle_menu_choice(8), 1)

    def test_start_setup(self):
        """Test that everything is ok with the method."""
        self.assertTrue(gf.start_setup(), True)

    def test_enter_names2p(self):
        """Test that everything is ok with the method."""
        self.assertIsNone(gf.enter_names2p(), None)

    def test_enter_names1p(self):
        """Test that everything is ok with the method."""
        self.assertIsNone(gf.enter_names1p(), None)

    def test_cheat(self):
        """Test that everything is ok with the method."""
        self.assertIsNone(gf.cheat(), None)


if __name__ == "__main__":
    unittest.main()
