import unittest
from intelligence import *


intell = Intelligence()


class TestIntelligence(unittest.TestCase):


    def test_name_of_ai(self):
        self.assertEqual(intell.nameOfAi(), "Weird Ai Yankovic")


if __name__ == '__main__':
    unittest.main()