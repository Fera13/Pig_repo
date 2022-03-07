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


if __name__ == "__main__":
    unittest.main()