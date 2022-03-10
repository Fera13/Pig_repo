import unittest
from player import Player
from file_handling import File_handling
""" """

fh = File_handling()
player = Player()
length = len(fh.readNameFiles("text_name_file.txt"))


class testPlayer(unittest.TestCase):
    """Tests the player class"""

    def test_setName_duplicates(self):
        """Testing if you can add duplicate names"""
        self.assertEqual(player.setName("name1"), length + 1)
        self.assertEqual(player.setName("name1"), length + 1)
        self.assertEqual(player.setName("name2"), length + 2)
        self.assertEqual(player.setName("name3"), length + 3)
        self.assertEqual(player.setName("name2"), length + 3)

    def test_updateName_wrongType(self):
        """Testing for wrong type entered"""
        with self.assertRaises(TypeError):
            player.updateName(2, "newName")

    def test_deleteName_wrongType(self):
        """Testing for wrong type entered"""
        with self.assertRaises(TypeError):
            player.deleteName(2)
            player.deleteName(2.5)

    def test_addCurrentNames_wrongType(self):
        """Testing for wrong type entered"""
        with self.assertRaises(TypeError):
            player.addCurrentNames("player1", 2)
            player.addCurrentNames(2, "player2")

    def test_addCurrentNames_result(self):
        """Testing that names get set"""
        self.assertEqual(player.addCurrentNames("name1", "name2"), "name1")


if __name__ == "__main__":
    unittest.main()
