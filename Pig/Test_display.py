import unittest
from display import *

dsplay = Display()

class TestDisplay(unittest.TestCase):
    
    def test_winner_wrong_type(self):
        with self.assertRaises(TypeError): dsplay.winner([])
        
    def test_game_menu_wrong_type(self):
        with self.assertRaises(TypeError): dsplay.gameMenu('2')
        
    def test_rules_wrong_type(self):
        with self.assertRaises(TypeError): dsplay.displayGameRules(5)
        
    def test_game_summary_wrong_type(self):
        with self.assertRaises(TypeError): dsplay.gameSummary(3, 4, '[3,2,6,8,9]', '[8,2,0,6,5]')
    
if __name__ == '__main__':
    unittest.main()