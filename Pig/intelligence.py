"""
This script is used to get amount of rolls and name for AI.

Authors: Farah, Alfred, Emil
"""
import random
from random import choice


class Intelligence:
    """The class for the AI."""

    def roll_amount_nor_har(self):
        """Determine roll amount for normal and hard AI."""
        roll_amount = random.randint(1, 7)
        return roll_amount

    def roll_amount_easy(self):
        """Determine roll amount for easy AI."""
        nums = [1, 2, 6, 5, 7]
        roll_amount = choice(nums)
        return roll_amount

    def name_of_ai(self):
        """Get name of AI."""
        ai_name = "Weird Ai Yankovic"
        return ai_name
