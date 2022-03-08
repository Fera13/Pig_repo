from random import randrange
from player import Player
from display import *


class dice:
    roundSum = 0
    amountOfRolls = 0
    display = Display()
    totalSum = 0

    def __init__(self):
        return None

    def roll(self, timesToRoll: int):
        if not isinstance(timesToRoll, int):
            raise TypeError("timesToRoll must be an integer")
        if timesToRoll <= 0:
            raise ValueError("times to roll has to be more than 0")
        else:
            self.roundSum = 0
            self.amountOfRolls = + 1
            
            for i in range(timesToRoll):
                rollNumber = randrange(1, 7)
                if rollNumber == 1:
                    self.roundSum = 0
                    print("Rolled a 1, and therefore recieved 0 points this round")
                    break
                else:
                    print("Rolled a " + str(rollNumber))
                    self.roundSum += rollNumber
            self.totalSum += self.roundSum

            # if total over 100, call winner method from display
            if self.totalSum >= 100:
                self.display.winner()

            return self.roundSum

    def getTotalSum(self):
        return self.totalSum

    def getAmountOfRolls(self):
        return self.amountOfRolls
