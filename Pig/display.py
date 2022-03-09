from player import *


playr = Player()


class Display:

    def winner(self, name:str):
        if not isinstance(name, str):
            raise TypeError("Something went wrong while trying to retrieve the winning players' name")
        print('\n', '-'*80)
        print(f'\n          Congratulations {name}, you have won the game!\n')
        print('-'*80, '\n')


    def gameMenu(self):
        notCorrect = True
        while notCorrect:
            print(f'\n                           THE PIG GAME')
            print(f'----------------------------------------------------------------------')
            print('1:  Start a one player game')
            print('2:  Start a two player game')
            print('3:  Update existing player name')
            print('4:  Delete existing player')
            print('5:  View highscore')
            print('6:  Show rules')
            print('7:  Exit game')
            print(f'----------------------------------------------------------------------\n')
            choice = int(input('Please enter your choice here: '))
            if not isinstance(choice, int):
                raise ValueError('You can only use numbers to choose an option')
            if choice in [1,2,3,4,5,6,7]:
                return choice
            else:
                print('Please enter a number from the available options')


    def displayGameRules(self):
        print('\nThe rules for Pig-Game are as following:\n')
        print('-  The player begins each turn by rolling the dice.')
        print('-  The player may roll as many times as they want in a round.')
        print('-  If the dice lands on a 1, the round ends and all points from the current round will be deducted.')
        print('-  For every other number on the dice the points relevant to the dice surface will add up to a round total')
        print('-  The first player to reach 100 points will be the victor!\n')


    def gameSummary(self, name:str, rolls:int):
        if not isinstance(name, str) or not isinstance(rolls, int):
            raise TypeError('The game summary is not available right now')
        print(f'\nHere is the amount of rolls for the player to reach 100 points\n')
        print(f'Name {"Amount of rounds":>35}')
        print(f'----------------------------------------------------------------------')
        print(f'{name:25}  {rolls:>6}')
        print(f'----------------------------------------------------------------------\n')


    def showPlayers(self, namelist: list[str]):
        length = 0
        amountOfNames = 0
        print(f'Here is the list of current players\n')
        print(f'-'*70)
        while length < len(namelist):
            print("")
            while (amountOfNames < 4 and length < len(namelist)):
                print(f'>{namelist[length]:15}', end=" ")
                length += 1
                amountOfNames += 1
            amountOfNames = 0
        print(f'\n\n')
        print(f'-'*70)
        print("\n")


    def viewGameProg2(self, player1: str, points1: int, player2: str, points2: int):
        if not isinstance(player1, str) or not isinstance(points1, int) or not isinstance(player2, str) or not isinstance(points2, int):
            raise TypeError("The game progress is not available right now")

        print(f"\n\nPlayer1: {player1:60} Player2: {player2}")
        print(f"Points: {points1:<61} Points: {points2}\n")


    def viewDifficulties(self):
        notCorrect = True
        while notCorrect:
            print(f'\nHere are the difficulties, which one do you dare to oppose?\n')
            print(f'1:  Easy Mode')
            print(f'2:  Normal Mode')
            print(f'3:  Hard Mode')
            print(f'4:  Go back to the main menu')
            choice = int(input(f'Please enter the number of the challenge you dare to try today. It is okay to be a coward. '))
            if not isinstance(choice, int):
                raise ValueError('You can only use numbers to choose an option')
            if choice in [1,2,3,4]:
                    return choice
                    
            else:
                    print('Please enter a number from the available options')

