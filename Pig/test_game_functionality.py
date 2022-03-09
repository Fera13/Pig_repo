import unittest
from game_functionality import *


gf = Game_functionality()


class testGameFunctionality(unittest.TestCase):


    def test_handleMenuChoice_wrongValue(self):
        with self.assertRaises(ValueError): gf.handleMenuChoice("hi")


if __name__ == '__main__':
    unittest.main()
    
