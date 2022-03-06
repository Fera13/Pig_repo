class Display:

    def winner(self, name:str):
        
        print(f'\n----------------------------------------------------------------------')
        print(f'\n          Congratulations {name}, you have won the game!')
        print(f'\n----------------------------------------------------------------------\n')
    
    
    def gameMenu(self):
        print(f'\n----------------------------------------------------------------------')
        print(f'\nEnter one of the following options:\n')
        print('1:  Play Pig-Game')
        print('2:  Show the the rules of Pig-Game')
        print('3:  Show the current highscores')
        print('4:  Quit')
        print(f'\n----------------------------------------------------------------------')
        
    def displayGameRules(self):
        print(f'\nThe rules for Pig-Game are as following:\n') 
        print('-  The player begins each turn by rolling the dice.')
        print('-  The player may roll as many times as they want in a round.')
        print('-  If the dice lands on a 1, the round ends and all points from the current round will be deducted.')
        print('-  As long as the dice does not land on a 1, the player may continue playing.')
        print('-  For every other number on the dice the points relevant to the dice surface will add up to a round total')
        print('-  The player may quit their round before each roll, with an exception of the first roll')
        print(f'-  The first player to reach 100 points will be the victor!\n')
    
    def gameSummary(self):
        roundCount = 1
        #I will need an object created with a list so that each round can be calculated and added into the list. 
        print(f'\nHere is a summary of all the points collected by the players in each round')
        for i in self:
            print(f'Round {roundCount} {self[i]:>10}')
            roundCount = roundCount + 1