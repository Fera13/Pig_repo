"""
This script is used to get amount of rolls and name for AI.

Authors: Farah, Alfred, Emil
"""
import random
from random import choice


class Intelligence:
    """The class for the AI."""

    def rollAmountNorHar(self):
        """Determine roll amount for normal and hard AI."""
        n = random.randint(1, 7)
        return n

    def rollAmountEasy(self):
        """Determine roll amount for easy AI."""
        nums = [1, 2, 6, 5, 7]
        n = choice(nums)
        return n

    def nameOfAi(self):
        """Get name of AI."""
        aiName = "Weird Ai Yankovic"
        return aiName
