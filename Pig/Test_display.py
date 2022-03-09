import unittest
from display import *

dplay = Display()


class TestDisplay(unittest.TestCase):
    def test_winner_wrong_type(self):
        with self.assertRaises(TypeError):
            dplay.winner(3)

    def test_game_summary_wrong_type(self):
        with self.assertRaises(TypeError):
            dplay.gameSummary(3, "hajhaj")

    def test_show_players(self):
        with self.assertRaises(TypeError):
            dplay.showPlayers(3)

    def test_view_game_prog(self):
        with self.assertRaises(TypeError):
            dplay.viewGameProg2(3, "k", 5, "o")

    def test_view_difficulties(self):
        with self.assertRaises(ValueError):
            dplay.viewDifficulties()

    def test_game_menu(self):
        with self.assertRaises(ValueError):
            dplay.gameMenu()


if __name__ == "__main__":
    unittest.main()
