"""
This class test highscore class.

Authors: Farah, Alfred, Emil
"""
import unittest
from high_score import HighScore

hs = HighScore()


class TestHighScore(unittest.TestCase):
    """Test the high score class."""

    def test_view_high_scores_wrong_type(self):
        """Test that an error will be raised if the wrong type of arguments \
is entered."""
        with self.assertRaises(ValueError):
            hs.view_high_scores("hi")

    def test_view_high_scores(self):
        """Test if the given list will be displayed right."""
        lis = [["Hi", 8], ["Hello", 6]]
        self.assertTrue(hs.view_high_scores(lis), True)

    def test_add_compare_high_scores(self):
        """Test that the high score dictionary will be returned after adding \
or replacing keys and values to it."""
        lis = [["Farah", 13], ["Developer", 9001]]
        self.assertListEqual(hs.add_compare_high_scores("Farah", 13), lis)
        lis = [["shhh", 3], ["Farah", 13], ["Developer", 9001]]
        self.assertListEqual(hs.add_compare_high_scores("shhh", 3), lis)
        lis = [["shhh", 3], ["maha", 7], ["Farah", 13], ["Developer", 9001]]
        self.assertListEqual(hs.add_compare_high_scores("maha", 7), lis)
        lis = [["kami", 1], ["shhh", 3], ["maha", 7], ["Farah", 13],
               ["Developer", 9001]]
        self.assertListEqual(hs.add_compare_high_scores("kami", 1), lis)
        lis = [["kami", 1], ["shhh", 3], ["suha", 4], ["maha", 7],
               ["Farah", 13]]
        self.assertListEqual(hs.add_compare_high_scores("suha", 4), lis)

    def test_get_high_score_list(self):
        """Test that the high score dictionary will be returned when asking \
to get it."""
        lis = [["kami", 1], ["shhh", 3], ["suha", 4], ["maha", 7],
               ["Farah", 13]]
        self.assertListEqual(hs.get_high_score_list(), lis)

    def test_add_compare_high_scores_wrong_name(self):
        """Test that an error will be raised if the wrong type of arguments \
is entered."""
        with self.assertRaises(ValueError):
            hs.add_compare_high_scores([], 2)

    def test_add_compare_high_scores_wrong_score(self):
        """Test that an error will be raised if the wrong type of arguments \
is entered."""
        with self.assertRaises(ValueError):
            hs.add_compare_high_scores("hi", "world")

    def test_update_high_score(self):
        """Test that the updated high score dictionary will be returned after \
changing a key in it."""
        lis = [["kami", 1], ["Fera", 3], ["suha", 4], ["maha", 7],
               ["Farah", 13]]
        self.assertListEqual(hs.update_high_score("shhh", "Fera"), lis)

    def test_update_high_score_wrong_type(self):
        """Test that an error will be raised if the wrong type of arguments \
is entered."""
        with self.assertRaises(ValueError):
            hs.add_compare_high_scores(3, "world")
        with self.assertRaises(ValueError):
            hs.add_compare_high_scores("eren", [])


if __name__ == "__main__":
    unittest.main()
