import unittest
from display import Display
""" """

dplay = Display()


class TestDisplay(unittest.TestCase):
    """Testing the Display class."""

    def test_winner_wrong_type(self):
        """Testing the winner method.
        Checking if a TypeError is raised.
        """
        with self.assertRaises(TypeError):
            dplay.winner(3)

    def test_game_summary_wrong_type(self):
        """Testing the gameSummary method.
        Checking if a TypeError is raised.
        """
        with self.assertRaises(TypeError):
            dplay.gameSummary(3, "hajhaj")

    def test_show_players(self):
        """Testing the showPlayers method.
        Checking if a TypeError is raised.
        """
        with self.assertRaises(TypeError):
            dplay.showPlayers(3)

    def test_view_game_prog(self):
        """Testing the viewProg method.
        Checking if a TypeError is raised.
        """
        with self.assertRaises(TypeError):
            dplay.viewProg(3, "k", 5, "o")

    def test_view_difficulties(self):
        """Testing the viewDifficulties method.
        Checking if a ValueError is raised.
        """
        with self.assertRaises(ValueError):
            dplay.viewDifficulties()

    def test_game_menu(self):
        """Testing the gameMenu method.
        Checking if a ValueError is raised.
        """
        with self.assertRaises(ValueError):
            dplay.gameMenu()


if __name__ == "__main__":
    unittest.main()
