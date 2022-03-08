import unittest
from player import *

player = Player()


class testPlayer(unittest.TestCase):

    def test_setName_duplicates(self):
        self.assertEqual(player.setName("name1"), 1)
        self.assertEqual(player.setName("name1"), 1)
        self.assertEqual(player.setName("name2"), 2)
        self.assertEqual(player.setName("name3"), 3)
        self.assertEqual(player.setName("name2"), 3)

    def test_addCurrentScore_wrongType(self):
        with self.assertRaises(TypeError):
            player.addCurrentScore("2", "Emil")
        with self.assertRaises(TypeError):
            player.addCurrentScore("Emil", 2)
        with self.assertRaises(TypeError):
            player.addCurrentScore(2, 2)

    def test_addCurrentScore_negativeValue(self):
        with self.assertRaises(ValueError):
            player.addCurrentScore(-2, "Emil")
        with self.assertRaises(ValueError):
            player.addCurrentScore(-1, "Emil")

    def test_updateName_wrongType(self):
        with self.assertRaises(TypeError):
            player.updateName(2, "newName")

    def test_deleteName_wrongType(self):
        with self.assertRaises(TypeError):
            player.deleteName(2)
            player.deleteName(2.5)
    
    def test_addCurrentNames_wrongType(self):
        with self.assertRaises(TypeError):
            player.addCurrentNames("player1", 2)
            player.addCurrentNames(2, "player2")

if __name__ == "__main__":
    unittest.main()
