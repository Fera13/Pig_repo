import unittest
from display import *

dsplay = Display()

class TestDisplay(unittest.TestCase):
    
    def testWinnerWrongType(self):
        with self.assertRaises(TypeError): dsplay.winner('Alfred')
        
    def testGameMenuWrongType(self):
        with self.assertRaises(TypeError): dsplay.gameMenu(5)
        
    def testRulesWrongType(self):
        with self.assertRaises(TypeError): dsplay.displayGameRules('s')
        
    def testGameSummaryWrongType(self):
        with self.assertRaises(TypeError): dsplay.gameSummary('Farah', 'Emil', [3,2,6,8,9], [8,2,0,6,5])
    
    if __name__ == '__main__':
        unittest.main()