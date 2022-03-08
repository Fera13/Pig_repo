

class Display:

    def winner(self, name:str):
        if not isinstance(name,str):
            raise TypeError("Something went wrong while trying to retrieve the winning players' name")

        print(f'\n----------------------------------------------------------------------')
        print(f'\n          Congratulations {name}, you have won the game!')
        print(f'\n----------------------------------------------------------------------\n')


    #def gameMenu(self):
        #notCorrect = True
        #while notCorrect:
            #print(f'\n----------------------------------------------------------------------')
            #print('1:  Start a one player game')
            #print('2:  Start a two player game')
            #print('3:  Update existing player name')
            #print('4:  Delete existing player')
            #print('5:  View highscore')
            #print('6:  Show rules')
            #print('7:  Exit game')
            #print(f'----------------------------------------------------------------------\n')
            #try:
                #choice = input('Please enter your choice here: ')
                #if choice in [1,2,3,4,5,6,7]:
                    #gameFunc.handleMenuChoice(choice)
                #else:
                    #print('Please enter a number from the available options')
            #except TypeError:
                #print('You can only use numbers to choose an option')


    def displayGameRules(self):
        notCorrect = True
        while notCorrect:
            print(f'\nThe rules for Pig-Game are as following:\n')
            print('-  The player begins each turn by rolling the dice.')
            print('-  The player may roll as many times as they want in a round.')
            print('-  If the dice lands on a 1, the round ends and all points from the current round will be deducted.')
            print('-  As long as the dice does not land on a 1, the player may continue playing.')
            print('-  For every other number on the dice the points relevant to the dice surface will add up to a round total')
            print('-  The player may quit their round before each roll, with an exception of the first roll')
            print(f'-  The first player to reach 100 points will be the victor!\n')
            try:
                choice = input('When you have read and understood the rules, please enter any letter of your choice to get back to the menu')
                if choice is str:
                    Display.gameMenu()
                else:
                    print('Please enter a letter to get back to the main menu')
            except TypeError:
                print('You can only use letters in the alphabet to get back to the main menu')



    def gameSummary(self, name:str, rolls:int):
        roundCount = 1
        if not isinstance(name, str) or not isinstance(rolls, int):
            raise TypeError('The game summary is not available right now')

        amountOfRolls = 'Amount of rolls'
        print(f'\nHere is the amount of rolls for the player to reach 100 points\n')
        print(f'Name {amountOfRolls:>35}')
        print(f'----------------------------------------------------------------------')
        print(f'{name}  {rolls:>25}')
        print(f'----------------------------------------------------------------------\n')


    def showPlayers(self, namelist:list[str]):
        if not isinstance(namelist,[str]):
            raise TypeError("The list of names could not be found at this moment")

        length = 0
        amountOfNames = 0
        print(f'Here is the list of current players\n----------------------------------------------------------------------')
        while length < len(namelist):
            print("")
            while (amountOfNames < 4 and length < len(namelist)):
                print(f'>{namelist[length]:15}', end=" ")
                length += 1
                amountOfNames += 1
            amountOfNames = 0
        print(f'\n\n----------------------------------------------------------------------\n')


    def viewGameProg2(player1: str, points1: int, player2: str, points2: int):
        if not isinstance(player1, str) or not isinstance(points1, int) or not isinstance(player2, str) or not isinstance(points2, int):
            raise TypeError("The game progress is not available right now")

        print(f"Player1: {player1:60} Player2: {player2}")
        print(f"Points: {points1:<61} Points: {points2}\n")