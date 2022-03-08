import unittest
from High_score import *


hs = High_score()

class testGameFunctionality(unittest.TestCase):
    
    def test_view_Highscores_wrongType(self):
        with self.assertRaises(TypeError): hs.view_HighScores("hi")
    
    
    def test_add_Compare_Highscores(self):
        d1 = {"Farah": 13}
        self.assertDictEqual(hs.add_Compare_Highscores("Farah", 13), d1)
        d2 = {"shhh": 3, "Farah": 13}
        self.assertDictEqual(hs.add_Compare_Highscores("shhh", 3), d2)
        d3 = {"shhh": 3, "maha": 7, "Farah": 13}
        self.assertDictEqual(hs.add_Compare_Highscores("maha", 7), d3)
        d4 = {"kamil": 1, "shhh": 3, "maha": 7, "Farah": 13}
        self.assertDictEqual(hs.add_Compare_Highscores("kamil", 1), d4)
        d5 = {"kamil": 1, "shhh": 3, "suha": 4, "maha": 7, "Farah": 13}
        self.assertDictEqual(hs.add_Compare_Highscores("suha", 4), d5)
        d6 = {"kamil": 1, "saby": 2, "shhh": 3, "suha": 4, "maha": 7}
        self.assertDictEqual(hs.add_Compare_Highscores("saby", 2), d6)
        

    def test_add_Compare_Highscores_wrongName(self):
        with self.assertRaises(TypeError): hs.add_Compare_Highscores([], 2)
        
        
    def test_add_Compare_Highscores_wrongscore(self):
        with self.assertRaises(TypeError): hs.add_Compare_Highscores("hi", "world")
    
    
    def test_update_High_Score(self):
        d1 = {'kamil': 1, 'saby': 2, 'Fera': 3, 'suha': 4, 'maha': 7}
        self.assertDictEqual(hs.update_High_Score("shhh", "Fera"), d1)
        
        
    def test_update_High_Score_wrongType(self):
        with self.assertRaises(TypeError): hs.add_Compare_Highscores(3, "world")
        with self.assertRaises(TypeError): hs.add_Compare_Highscores("eren", [])
        
        
    def test_get_HighScore_Dic(self):
        d1 = {'kamil': 1, 'saby': 2, 'shhh': 3, 'suha': 4, 'maha': 7}
        self.assertDictEqual(hs.get_HighScore_Dic(), d1)
    
if __name__ == '__main__':
    unittest.main()