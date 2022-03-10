import unittest
from game_functionality import Game_functionality


gf = Game_functionality()


class testGameFunctionality(unittest.TestCase):
  
    def test_handleMenuChoice_wrongValue(self):
        '''Tests that an error will be raised if the wrong type of arguments\
             is entered'''
        with self.assertRaises(ValueError):
            gf.handleMenuChoice("hi")


if __name__ == "__main__":
    unittest.main()
