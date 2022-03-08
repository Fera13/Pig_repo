from random import randrange
from player import Player
from display import *


class dice:
    roundSum = 0
    winnerName = ""
    amountOfRolls = [0, 0]
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
            if self.turn == 0:
                self.amountOfRolls[0] = + 1
                self.player.addCurrentScore(self.roundSum, currentPl[0])
                self.turn = 1
            else:
                self.amountOfRolls[1] = + 1
                self.player.addCurrentScore(self.roundSum, currentPl[1])
                self.turn = 0

            # if total over 100
            if self.totalSum >= 100:
                pl = self.player.getCurrentNames()
                if self.turn == 0:
                    self.winnerName = pl[0]
                else:
                    self.winnerName = pl[1]
                # self.display.winner()

            return self.roundSum

    def getWinnerName(self):
        return self.winnerName

    def getAmountOfRolls(self, playerNumber: int):
        if playerNumber == 0:
            return self.amountOfRolls[0]
        else:
            return self.amountOfRolls[1]
