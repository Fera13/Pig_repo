import random
from secrets import choice


class Intelligence:
    """The class for the AI."""

    def rollAmountNorHar(self):
        """Takes no parameters.
        Determines how many rolls the hard and normal AI should do each round.
        Returns the amount.
        """
        n = random.randint(1, 7)
        return n

    def rollAmountEasy(self):
        """Takes no parameters.
        Determines how many rolls the easy AI should do each round.
        Returns the amount.
        """
        nums = [1, 2, 6, 5, 7]
        n = choice(nums)
        return n

    def nameOfAi(self):
        """Takes no parameters.
        A place where the name of the AI is stored.
        Returns the name.
        """
        aiName = "Weird Ai Yankovic"
        return aiName
