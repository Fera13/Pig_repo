"""
This script is used to handle dice roll operations for a dice game.

Authors: Farah, Alfred, Emil
"""
from random import randrange, choice
from player import Player
from display import Display

player = Player()
dis = Display()


class Dice:
    """Do roll for player and AI, reset scores and return winner."""

    winnerName = ""
    amountOfRounds = [0, 0]
    scores = player.getCurrentScore()
    totalSum1 = scores[0]
    totalSum2 = scores[1]
    turn = 0
    score1 = 0
    score2 = 0

    def roll(self, timesToRoll: int):
        """Take one parameter: int, do roll for the times entered."""
        roundSum = 0
        if not isinstance(timesToRoll, int):
            raise TypeError("timesToRoll must be an integer")
        if timesToRoll <= 0:
            raise ValueError("times to roll has to be more than 0")
        names = player.getCurrentNames()
        i = 0
        while i < timesToRoll:
            rollNumber = randrange(1, 7)
            if rollNumber != 1:
                i += 1
                print("Rolled a " + str(rollNumber))
                roundSum += rollNumber
            else:
                roundSum = 0
                print(
                    "Rolled a 1, and therefore recieved 0 points \
                    this round"
                )
                break
        if self.turn == 0:
            self.totalSum1 += roundSum
            self.amountOfRounds[0] += 1
            self.turn = 1
            if self.totalSum1 >= 100:
                self.winnerName = names[0]
                self.turn = 0
        else:
            self.totalSum2 += roundSum
            self.amountOfRounds[1] += 1
            self.turn = 0
            if self.totalSum2 >= 100:
                self.winnerName = names[1]
        dis.viewProg(names[0], self.totalSum1, names[1], self.totalSum2)

    def hardAiRoll(self, rollNum: int):
        """Take one parameter: int and roll for the AI."""
        if not isinstance(rollNum, int):
            raise TypeError("rollNum has be to an int")
        if rollNum <= 0:
            raise ValueError("rollNum has to be more than 0")
        roundSum = 0
        names = player.getCurrentNames()
        i = 0
        while i < rollNum:
            num = [1, 2, 3, 4, 4, 5, 5, 6, 6]
            rollResult = choice(num)
            if rollResult != 1:
                print("Rolled a " + str(rollResult))
                roundSum += rollResult
                i += 1
            else:
                roundSum = 0
                print(
                    "Even geniuses roll a 1, Weird Ai Yankovic got 0 points\
                        this round"
                )
                break
        self.totalSum2 += roundSum
        self.amountOfRounds[1] += 1
        self.turn = 0
        if self.totalSum2 >= 100:
            self.winnerName = names[1]
            self.turn = 0
        dis.viewProg(names[0], self.totalSum1, names[1], self.totalSum2)

    def easyAiRoll(self, rollNum: int):
        """Take one parameter: int and roll for the AI."""
        if not isinstance(rollNum, int):
            raise TypeError("rollNum has be to an int")
        if rollNum <= 0:
            raise ValueError("rollNum has to be more than 0")
        roundSum = 0
        names = player.getCurrentNames()
        i = 0
        while i < rollNum:
            num = [1, 2, 3, 4, 5, 6, 1, 1]
            rollResult = choice(num)
            if rollResult != 1:
                print("Rolled a " + str(rollResult))
                roundSum += rollResult
                i += 1
            else:
                roundSum = 0
                print(
                    "Even geniuses roll a 1, Weird Ai Yankovic got 0 points\
                        this round"
                )
                break
        self.totalSum2 += roundSum
        self.amountOfRounds[1] += 1
        self.turn = 0
        if self.totalSum2 >= 100:
            self.winnerName = names[1]
            self.turn = 0
        dis.viewProg(names[0], self.totalSum1, names[1], self.totalSum2)

    def resetTotals(self):
        """Reset the total sum for both players."""
        self.totalSum1 = 0
        self.totalSum2 = 0
        return self.totalSum1

    def resetRoundNum(self):
        """Reset the amount of rounds for both players."""
        self.amountOfRounds[0] = 0
        self.amountOfRounds[1] = 0

    def getWinnerName(self):
        """Return the name of the winner."""
        return self.winnerName

    def getTotalSum1(self):
        """Return the total sum of the first player."""
        return self.totalSum1

    def getTotalSum2(self):
        """Return the total sum of the second player."""
        return self.totalSum2

    def getAmountOfRounds(self, winnerName: str):
        """Take one parameter: str and return the amount of rounds."""
        names = player.getCurrentNames()
        if winnerName == names[0]:
            return self.amountOfRounds[0]
        return self.amountOfRounds[1]

    def cheatDice(self):
        """Set the total sum of the first player to 99."""
        self.totalSum1 = 99
        return self.totalSum1
