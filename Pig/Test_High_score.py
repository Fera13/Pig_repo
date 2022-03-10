"""
This class tests highscore class.

Authors: Farah, Alfred, Emil
"""
import unittest
from high_score import High_score

hs = High_score()


class TestHighScore(unittest.TestCase):
    """Tests the high score class."""

    def test_view_highscores_wrong_type(self):
        """Tests that an error will be raised if the wrong type of arguments \
            is entered."""
        with self.assertRaises(ValueError):
            hs.view_high_scores("hi")

    def test_add_compare_high_scores(self):
        """Tests that the high score dictionary will be returned after adding \
            or replacing keys and values to it."""
        d1 = {"Farah": 13, "Developer": 9001}
        self.assertDictEqual(hs.add_compare_highscores("Farah", 13), d1)
        d2 = {"shhh": 3, "Farah": 13, "Developer": 9001}
        self.assertDictEqual(hs.add_compare_highscores("shhh", 3), d2)
        d3 = {"shhh": 3, "maha": 7, "Farah": 13, "Developer": 9001}
        self.assertDictEqual(hs.add_compare_highscores("maha", 7), d3)
        d4 = {"kamil": 1, "shhh": 3, "maha": 7, "Farah": 13, "Developer": 9001}
        self.assertDictEqual(hs.add_compare_highscores("kamil", 1), d4)
        d5 = {"kamil": 1, "shhh": 3, "suha": 4, "maha": 7, "Farah": 13}
        self.assertDictEqual(hs.add_compare_highscores("suha", 4), d5)

    def test_get_highScore_dic(self):
        """Tests that the high score dictionary will be returned when asking\
             to get it."""
        d1 = {"kamil": 1, "shhh": 3, "suha": 4, "maha": 7, "Farah": 13}
        self.assertDictEqual(hs.get_highScore_dic(), d1)

    def test_add_compare_highscores_wrong_name(self):
        """Tests that an error will be raised if the wrong type of arguments\
             is entered."""
        with self.assertRaises(ValueError):
            hs.add_compare_highscores([], 2)

    def test_add_compare_highscores_wrong_score(self):
        """Tests that an error will be raised if the wrong type of arguments\
             is entered."""
        with self.assertRaises(ValueError):
            hs.add_compare_highscores("hi", "world")

    def test_update_high_score(self):
        """Tests that the updated high score dictionary will be returned after\
             changing a key in it."""
        d1 = {"kamil": 1, "Fera": 3, "suha": 4, "maha": 7, "Farah": 13}
        self.assertDictEqual(hs.update_high_score("shhh", "Fera"), d1)

    def test_update_high_score_wrong_type(self):
        """Tests that an error will be raised if the wrong type of arguments\
             is entered."""
        with self.assertRaises(ValueError):
            hs.add_compare_highscores(3, "world")
        with self.assertRaises(ValueError):
            hs.add_compare_highscores("eren", [])


if __name__ == "__main__":
    unittest.main()
