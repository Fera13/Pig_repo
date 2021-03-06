"""
This tets the intelligence class.

Authors: Farah, Alfred, Emil
"""
import unittest
from intelligence import Intelligence


intell = Intelligence()


class TestIntelligence(unittest.TestCase):
    """Testing the Intelligence class."""

    def test_roll_amount_nor_har(self):
        """Testing the rollAmountNorHar method \
Checking if the return is a number from 1 to 6."""
        self.assertTrue(1 <= intell.roll_amount_nor_har() <= 7)

    def test_roll_amount_easy(self):
        """Testing the rollAmountEasy method \
Checking if the return is a number from 1 to 6."""
        self.assertTrue(1 <= intell.roll_amount_nor_har() <= 7)

    def test_name_of_ai(self):
        """Testing the nameOfAi method \
Checking if the return is correct name of the AI."""
        self.assertEqual(intell.name_of_ai(), "Weird Ai Yankovic")


if __name__ == "__main__":
    unittest.main()
