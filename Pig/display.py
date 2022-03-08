class Display:

    def winner(self, name:str):
        if not isinstance(name,str):
            raise TypeError("Something went wrong while trying to retrieve the winning players' name")
            
        print(f'\n----------------------------------------------------------------------')
        print(f'\n          Congratulations {name}, you have won the game!')
        print(f'\n----------------------------------------------------------------------\n')
       
        
    
    
    def gameMenu(self):
        notCorrect = True
        while notCorrect:
            print(f'\n----------------------------------------------------------------------\n')
            print('1:  Start a one player game')
            print('2:  Start a two player game')
            print('3:  Update existing player name')
            print('4:  Delete existing player')
            print('5:  View highscore')
            print('6:  Show rules')
            print('7:  Exit game')
            print(f'\n----------------------------------------------------------------------\n')
            try:
                choice = input('Please enter your choice here: ')
                if choice in [1,2,3,4,5,6,7]:
                    return choice
                else: 
                    print('Please enter a number from the available options')
            except TypeError:
                print('You can only use numbers to choose an option')


    def displayGameRules():
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
            
                
    
    def gameSummary(self, name_1:str, name_2:str, score_1:list[int], score_2:list[int]):
        roundCount = 1
        print(f'\nHere is a summary of all the points collected by the players in each round')
        print(f'\n----------------------------------------------------------------------\n')
        print(f'Rounds {name_1:>10} {name_2:>10}')
        for i in self:
            print(f'Round {roundCount} {score_1[i]:>20} {score_2[i]:>20}')
            roundCount = roundCount + 1
        print(f'\n----------------------------------------------------------------------\n')