from random import randrange
from player import Player

class Dice:
    roundSum = 0
    amountOfRolls = 0

    # SHOULD MAYBE BE IN PLAYER CLASS? RETURN FROM ROLL ROUND SUM AND ADD TO TOTAL IN PLAYER?
    totalSum = 0

    def roll(self, timesToRoll):
        '''Rolls the amount of times entered, increments amountOfROlls and returns roundSum'''
        self.roundSum = 0
        self.amountOfRolls =+ 1

        for i in range(timesToRoll):
            rollNumber = randrange(1, 7)
            if rollNumber == 1:
                self.roundSum = 0
                print("You rolled a 1, and therefore recieved 0 points this round")
                break
            else:
                print("you rolled " + str(rollNumber))
                self.roundSum += rollNumber
        self.totalSum += self.roundSum
        return self.roundSum
    
    def getTotalSum(self):
        return self.totalSum
     



class main:
    player = Player("Emil")

    dice = Dice()
    for i in range(2):
        dice.roll(2)
        print("--------------")
    print(dice.getTotalSum())

    player.setScore(dice.getTotalSum())

    print(player.getScore())


    