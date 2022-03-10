"""
This script is used to test Display.

Authors: Farah, Alfred, Emil
"""
import unittest
from display import Display


dplay = Display()


class TestDisplay(unittest.TestCase):
    """Testing the Display class."""

    def test_winner_wrong_type(self):
        """Test if the winner method raises TypeError."""
        with self.assertRaises(TypeError):
            dplay.winner(3)

    def test_game_summary_wrong_type(self):
        """Test if the gameSummary method raises TypeError."""
        with self.assertRaises(TypeError):
            dplay.gameSummary(3, "hajhaj")

    def test_show_players(self):
        """Test if the showPlayers method raises TypeError."""
        with self.assertRaises(TypeError):
            dplay.showPlayers(3)

    def test_view_prog(self):
        """Test if the viewProg method raises TypeError."""
        with self.assertRaises(TypeError):
            dplay.viewProg(3, "k", 5, "o")

    def test_view_difficulties(self):
        """Test if the viewDifficulties method raises ValueError."""
        with self.assertRaises(ValueError):
            dplay.viewDifficulties()

    def test_game_menu(self):
        """Test if the gameMeny method raises ValueError."""
        with self.assertRaises(ValueError):
            dplay.gameMenu()


if __name__ == "__main__":
    unittest.main()
