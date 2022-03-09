import unittest
from intelligence import *


intell = Intelligence()


class TestIntelligence(unittest.TestCase):
    def test_roll_amount_nor_har(self):
        self.assertTrue(1 <= intell.rollAmountNorHar() <= 7)

    def test_roll_amount_easy(self):
        self.assertTrue(1 <= intell.rollAmountEasy() <= 7)

    def test_name_of_ai(self):
        self.assertEqual(intell.nameOfAi(), "Weird Ai Yankovic")


if __name__ == "__main__":
    unittest.main()
