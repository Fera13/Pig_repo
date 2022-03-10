"""
This class tests highscore class.

Authors: Farah, Alfred, Emil
"""
import unittest
from high_score import High_score

hs = High_score()


class testHighScore(unittest.TestCase):
    """Tests the high score class."""

    def test_view_Highscores_wrongType(self):
        """Tests that an error will be raised if the wrong type of arguments \
            is entered."""
        with self.assertRaises(ValueError):
            hs.view_HighScores("hi")

    def test_add_Compare_Highscores(self):
        """Tests that the high score dictionary will be returned after adding \
            or replacing keys and values to it."""
        d1 = {"Farah": 13, "Developer": 9001}
        self.assertDictEqual(hs.add_Compare_Highscores("Farah", 13), d1)
        d2 = {"shhh": 3, "Farah": 13, "Developer": 9001}
        self.assertDictEqual(hs.add_Compare_Highscores("shhh", 3), d2)
        d3 = {"shhh": 3, "maha": 7, "Farah": 13, "Developer": 9001}
        self.assertDictEqual(hs.add_Compare_Highscores("maha", 7), d3)
        d4 = {"kamil": 1, "shhh": 3, "maha": 7, "Farah": 13, "Developer": 9001}
        self.assertDictEqual(hs.add_Compare_Highscores("kamil", 1), d4)
        d5 = {"kamil": 1, "shhh": 3, "suha": 4, "maha": 7, "Farah": 13}
        self.assertDictEqual(hs.add_Compare_Highscores("suha", 4), d5)

    def test_get_HighScore_Dic(self):
        """Tests that the high score dictionary will be returned when asking\
             to get it."""
        d1 = {"kamil": 1, "shhh": 3, "suha": 4, "maha": 7, "Farah": 13}
        self.assertDictEqual(hs.get_HighScore_Dic(), d1)

    def test_add_Compare_Highscores_wrongName(self):
        """Tests that an error will be raised if the wrong type of arguments\
             is entered."""
        with self.assertRaises(ValueError):
            hs.add_Compare_Highscores([], 2)

    def test_add_Compare_Highscores_wrongscore(self):
        """Tests that an error will be raised if the wrong type of arguments\
             is entered."""
        with self.assertRaises(ValueError):
            hs.add_Compare_Highscores("hi", "world")

    def test_update_High_Score(self):
        """Tests that the updated high score dictionary will be returned after\
             changing a key in it."""
        d1 = {"kamil": 1, "Fera": 3, "suha": 4, "maha": 7, "Farah": 13}
        self.assertDictEqual(hs.update_High_Score("shhh", "Fera"), d1)

    def test_update_High_Score_wrongType(self):
        """Tests that an error will be raised if the wrong type of arguments\
             is entered."""
        with self.assertRaises(ValueError):
            hs.add_Compare_Highscores(3, "world")
        with self.assertRaises(ValueError):
            hs.add_Compare_Highscores("eren", [])


if __name__ == "__main__":
    unittest.main()
