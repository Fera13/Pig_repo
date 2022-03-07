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

    def test_setScore_wrongType(self):
        with self.assertRaises(TypeError): player.setScore("emil", "2")
        with self.assertRaises(TypeError): player.setScore(2, "2")
        with self.assertRaises(TypeError): player.setScore(2, 2)
    
    def test_setScore_negativeValue(self):
        with self.assertRaises(ValueError): player.setScore("emil", -2)
        with self.assertRaises(ValueError): player.setScore("emil", -1)

if __name__ == "__main__":
    unittest.main()