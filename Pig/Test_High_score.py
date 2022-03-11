"""
This class tests highscore class.

Authors: Farah, Alfred, Emil
"""
import unittest
from high_score import HighScore

hs = HighScore()


class TestHighScore(unittest.TestCase):
    """Tests the high score class."""

    def test_view_high_scores_wrong_type(self):
        """Tests that an error will be raised if the wrong type of arguments \
is entered."""
        with self.assertRaises(ValueError):
            hs.view_high_scores("hi")

    def test_add_compare_high_scores(self):
        """Tests that the high score dictionary will be returned after adding \
or replacing keys and values to it."""
        dic = {"Farah": 13, "Developer": 9001}
        self.assertDictEqual(hs.add_compare_high_scores("Farah", 13), dic)
        dic = {"shhh": 3, "Farah": 13, "Developer": 9001}
        self.assertDictEqual(hs.add_compare_high_scores("shhh", 3), dic)
        dic = {"shhh": 3, "maha": 7, "Farah": 13, "Developer": 9001}
        self.assertDictEqual(hs.add_compare_high_scores("maha", 7), dic)
        dic = {"kami": 1, "shhh": 3, "maha": 7, "Farah": 13, "Developer": 9001}
        self.assertDictEqual(hs.add_compare_high_scores("kami", 1), dic)
        dic = {"kami": 1, "shhh": 3, "suha": 4, "maha": 7, "Farah": 13}
        self.assertDictEqual(hs.add_compare_high_scores("suha", 4), dic)

    def test_get_high_score_dic(self):
        """Tests that the high score dictionary will be returned when asking \
to get it."""
        dic = {"kami": 1, "shhh": 3, "suha": 4, "maha": 7, "Farah": 13}
        self.assertDictEqual(hs.get_high_score_dic(), dic)

    def test_add_compare_high_scores_wrong_name(self):
        """Tests that an error will be raised if the wrong type of arguments \
is entered."""
        with self.assertRaises(ValueError):
            hs.add_compare_high_scores([], 2)

    def test_add_compare_high_scores_wrong_score(self):
        """Tests that an error will be raised if the wrong type of arguments \
is entered."""
        with self.assertRaises(ValueError):
            hs.add_compare_high_scores("hi", "world")

    def test_update_high_score(self):
        """Tests that the updated high score dictionary will be returned after \
changing a key in it."""
        dic = {"kami": 1, "Fera": 3, "suha": 4, "maha": 7, "Farah": 13}
        self.assertDictEqual(hs.update_high_score("shhh", "Fera"), dic)

    def test_update_high_score_wrong_type(self):
        """Tests that an error will be raised if the wrong type of arguments \
is entered."""
        with self.assertRaises(ValueError):
            hs.add_compare_high_scores(3, "world")
        with self.assertRaises(ValueError):
            hs.add_compare_high_scores("eren", [])


if __name__ == "__main__":
    unittest.main()
