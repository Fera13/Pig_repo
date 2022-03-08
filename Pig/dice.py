from random import randrange
from player import Player
from display import *


class dice:
    roundSum = 0
    winner = ""
    amountOfRolls = 0
    display = Display()
    player = Player()
    totalSum = 0
    turn = 0

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
            
            currentPl = self.player.getCurrentNames()
            if turn == 0:
                self.player.addCurrentScore(roundSum, currentPl[0])
                turn = 1
            else:
                self.player.addCurrentScore(roundSum, currentPl[1])
                turn = 0

            

            # if total over 100, call winner method from display
            if self.totalSum >= 100:
                self.display.winner()

            return self.roundSum


    def getAmountOfRolls(self):
        return self.amountOfRolls
