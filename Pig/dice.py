from random import *
from player import Player
from display import *

player = Player()
dis = Display()

class dice:
    winnerName = ""
    amountOfRolls = [0, 0]
    scores = player.getCurrentScore()
    totalSum1 = scores[0]
    totalSum2 = scores[1]
    turn = 0
    score1 = 0
    score2 = 0


    def __init__(self):
        return None


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
            scores = player.getCurrentScore()
            
            if self.turn == 0:
                self.totalSum1 += roundSum
                self.amountOfRolls[0] += 1
                    # player.addCurrentScore(self.totalSum1, names[0])
                    # player.addCurrentScore(self.totalSum2, names[1])
                    # dis.viewGameProg2(names[0], self.totalSum1, names[1], self.totalSum2)
                self.turn = 1
                print(self.totalSum1)
                if self.totalSum1 >= 100:
                    self.winnerName = names[0]
                    print(self.winnerName)
                    dis.winner(self.winnerName)
                    self.turn = 1
            else:
                self.totalSum2 += roundSum
                self.amountOfRolls[1] += 1
                # player.addCurrentScore(self.totalSum1, names[0])
                # player.addCurrentScore(self.totalSum2, names[1])
                self.turn = 0
                print(self.totalSum2)
                if self.totalSum2 >= 100:
                    self.winnerName = names[1]
                    print(self.winnerName)
                    dis.winner(self.winnerName)
                    self.turn = 1
            dis.viewGameProg2(names[0], self.totalSum1, names[1], self.totalSum2)
                
            # if self.totalSum >= 100:
            #     if self.turn == 0:
            #         self.winnerName = pl[0]
            #     else:
            #         self.winnerName = pl[1]
            
            # currentPl = self.player.getCurrentNames()
            # if self.turn == 0:
            #     self.amountOfRolls[0] = + 1
            #     self.player.addCurrentScore(self.roundSum, currentPl[0])
            #     self.turn = 1
            # else:
            #     self.amountOfRolls[1] = + 1
            #     self.player.addCurrentScore(self.roundSum, currentPl[1])
            #     self.turn = 0

            # if total over 100
            
                # self.display.winner()
    def hardAiRoll(self, rollNum: int):
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
        self.amountOfRolls[1] += 1
        self.turn = 0
        print(self.totalSum2)
        dis.viewGameProg2(names[0], self.totalSum1, names[1], self.totalSum2)


    def resetTotals(self):
        self.totalSum1 = 0
        self.totalSum2 = 0


    def getWinnerName(self):
        return self.winnerName


    def getTotalSum1(self):
        return self.totalSum1


    def getTotalSum2(self):
        return self.totalSum2


    def getAmountOfRolls(self, playerName: str):
        names = player.getCurrentNames()
        if playerName == names[0]:
            return self.amountOfRolls[0]
        else:
            return self.amountOfRolls[1]
    
    
    def cheatDice(self):
        self.totalSum1 = 99
        return self.totalSum1

