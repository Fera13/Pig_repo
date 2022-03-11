"""
This tets the player class.

Authors: Farah, Alfred, Emil
"""
import unittest
from player import Player
from file_handling import FileHandling


fh = FileHandling()
player = Player()
LENGTH = len(fh.read_name_files("Pig/text_name_file.txt"))


class TestPlayer(unittest.TestCase):
    """Tests the player class."""

    def test_set_name_duplicates(self):
        """Testing if you can add duplicate names."""
        self.assertEqual(player.set_name("name1"), LENGTH + 1)
        self.assertEqual(player.set_name("name2"), LENGTH + 2)
        self.assertEqual(player.set_name("name3"), LENGTH + 3)

    def test_update_name_wrong_type(self):
        """Testing for wrong type entered."""
        with self.assertRaises(TypeError):
            player.update_name(2, "newName")

    def test_delete_name_wrong_type(self):
        """Testing for wrong type entered."""
        with self.assertRaises(TypeError):
            player.delete_name(2)
            player.delete_name(2.5)

    def test_add_current_names_wrong_type(self):
        """Testing for wrong type entered."""
        with self.assertRaises(TypeError):
            player.add_current_names("player1", 2)
            player.add_current_names(2, "player2")

    def test_add_current_names_result(self):
        """Testing that names get set."""
        self.assertEqual(player.add_current_names("name1", "name2"), "name1")


if __name__ == "__main__":
    unittest.main()
