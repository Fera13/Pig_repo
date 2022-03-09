from random import *
from player import Player
from display import *


player = Player()
dis = Display()


class Dice:

    winnerName = ""
    amountOfRounds = [0, 0]
    scores = player.getCurrentScore()
    totalSum1 = scores[0]
    totalSum2 = scores[1]
    turn = 0
    score1 = 0
    score2 = 0


    def roll(self, timesToRoll: int):
        roundSum = 0
        if not isinstance(timesToRoll, int):
            raise TypeError("timesToRoll must be an integer")
        if timesToRoll <= 0:
            raise ValueError("times to roll has to be more than 0")
        else:
            names = player.getCurrentNames()
            for i in range(timesToRoll):
                rollNumber = randrange(1, 7)
                if rollNumber == 1:
                    roundSum = 0
                    print("Rolled a 1, and therefore recieved 0 points this round")
                    break
                else:
                    print("Rolled a " + str(rollNumber))
                    roundSum += rollNumber
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
            dis.viewGameProg2(names[0], self.totalSum1, names[1], self.totalSum2)


    def hardAiRoll(self, rollNum: int):
        if not isinstance(rollNum, int):
            raise TypeError("rollNum has be to an int")
        if rollNum <= 0:
            raise ValueError("rollNum has to be more than 0")
        roundSum = 0
        names = player.getCurrentNames()
        for i in range(rollNum):
            num = [1, 2, 3, 4, 4, 5, 5, 6, 6]
            rollResult = choice(num)
            if rollResult == 1:
                roundSum = 0
                print("Even geniuses roll a 1, Weird Ai Yankovic got 0 points this round")
                break
            else:
                print("Rolled a " + str(rollResult))
                roundSum += rollResult
        self.totalSum2 += roundSum
        self.amountOfRounds[1] += 1
        self.turn = 0
        if self.totalSum2 >= 100:
            self.winnerName = names[1]
            self.turn = 0
        dis.viewGameProg2(names[0], self.totalSum1, names[1], self.totalSum2)


    def easyAiRoll(self, rollNum: int):
        if not isinstance(rollNum, int):
            raise TypeError("rollNum has be to an int")
        if rollNum <= 0:
            raise ValueError("rollNum has to be more than 0")
        roundSum = 0
        names = player.getCurrentNames()
        for i in range(rollNum):
            num = [1, 2, 3, 4, 5, 6, 1, 1]
            rollResult = choice(num)
            if rollResult == 1:
                roundSum = 0
                print("Even geniuses roll a 1, Weird Ai Yankovic got 0 points this round")
                break
            else:
                print("Rolled a " + str(rollResult))
                roundSum += rollResult
        self.totalSum2 += roundSum
        self.amountOfRounds[1] += 1
        self.turn = 0
        if self.totalSum2 >= 100:
            self.winnerName = names[1]
            self.turn = 0
        dis.viewGameProg2(names[0], self.totalSum1, names[1], self.totalSum2)


    def resetTotals(self):
        self.totalSum1 = 0
        self.totalSum2 = 0
        return self.totalSum1


    def getWinnerName(self):
        return self.winnerName


    def getTotalSum1(self):
        return self.totalSum1


    def getTotalSum2(self):
        return self.totalSum2


    def getAmountOfRounds(self, winnerName: str):
        names = player.getCurrentNames()
        if winnerName == names[0]:
            return self.amountOfRounds[0]
        else:
            return self.amountOfRounds[1]


    def cheatDice(self):
        self.totalSum1 = 99
        return self.totalSum1
