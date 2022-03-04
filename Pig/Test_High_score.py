import unittest
from High_score import *

class testGameFunctionality(unittest.TestCase):
    
    def test_view_Highscores_wrongDic(self):
        with self.assertRaises(TypeError): High_score.view_HighScores(dict[int: str])
    
    
    def test_view_Highscores_wrongType(self):
        with self.assertRaises(TypeError): High_score.view_HighScores("hi")
    
    
    def test_add_Compare_Highscores(self):
        d1 = {"Farah": 13}
        self.assertDictEqual(High_score.add_Compare_Highscores("Farah", 13), d1)
        d2 = {"shhh": 3, "Farah": 13}
        self.assertDictEqual(High_score.add_Compare_Highscores("shhh", 3), d2)
        d3 = {"shhh": 3, "maha": 7, "Farah": 13}
        self.assertDictEqual(High_score.add_Compare_Highscores("maha", 7), d3)
        d4 = {"kamil": 1, "shhh": 3, "maha": 7, "Farah": 13}
        self.assertDictEqual(High_score.add_Compare_Highscores("kamil", 1), d4)
        d5 = {"kamil": 1, "shhh": 3, "suha": 4, "maha": 7, "Farah": 13}
        self.assertDictEqual(High_score.add_Compare_Highscores("suha", 4), d5)
        d6 = {"kamil": 1, "saby": 2, "shhh": 3, "suha": 4, "maha": 7}
        self.assertDictEqual(High_score.add_Compare_Highscores("saby", 2), d6)
        

    def test_add_Compare_Highscores_wrongName(self):
        with self.assertRaises(TypeError): High_score.add_Compare_Highscores([], 2)
        
        
    def test_add_Compare_Highscores_wrongscore(self):
        with self.assertRaises(TypeError): High_score.add_Compare_Highscores("hi", "world")
    
if __name__ == '__main__':
    unittest.main()