from Game_functionality import *

gf = Game_functionality()

def gameMenu(self):
        notCorrect = True
        while notCorrect:
            print(f'                          THE PIG GAME')
            print(f'\n----------------------------------------------------------------------')
            print('1:  Start a one player game')
            print('2:  Start a two player game')
            print('3:  Update existing player name')
            print('4:  Delete existing player')
            print('5:  View highscore')
            print('6:  Show rules')
            print('7:  Exit game')
            print(f'----------------------------------------------------------------------\n')
            try:
                choice = input('Please enter your choice here: ')
                if choice in [1,2,3,4,5,6,7]:
                    gf.handleMenuChoice(choice)
                else:
                    print('Please enter a number from the available options')
            except TypeError:
                print('You can only use numbers to choose an option')
