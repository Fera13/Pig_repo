import rlcompleter
from High_score import *
from display import *
from player import *
from dice import *

currentPlayer = "player1's turn"
currentPlayer1 = "player1's turn"

hs = High_score()
disp = Display()
playr = Player()
dise = dice()

class Game_functionality:
    
    def handleMenuChoice(self, choice: int):
        if choice == 1:
            self.enter_Names1()
            # start game
        elif choice == 2:
            self.enter_Names2p()
            # start game
        elif choice == 3:
            names = playr.getNames()
            disp.showPlayers(names)
            name = input("Enter the name you want to update: ")
            newName = input("Enter the new updated name: ")
            playr.updateName(name, newName)
            hs.update_High_Score(name, newName)
        elif choice == 4:
            names = playr.getNames()
            disp.showPlayers(names)
            name = input("\nEnter the name you want to delete: ")
            playr.deleteName(name)
        elif choice == 5:
            hsDic = {}
            hsDic == hs.get_HighScore_Dic()
            hs.view_HighScores(hsDic)
        elif choice == 6:
            disp.displayGameRules()
        else:
            quit()
    
    
    def enter_Names2p(self):
        names = playr.getNames()
        disp.showPlayers(names)
        name = input("Enter the name of player1(note: if you already have your name in the list, enter it): ")
        name2 = input("Enter the name of player2(note: if you already have your name in the list, enter it): ")
        playr.setName(name)
        playr.setName(name2)
        playr.addCurrentScore(0, name)
        playr.addCurrentScore(0, name2)
        playr.addCurrentNames(name, name2)
        self.startGame2p()
        
        #method 
        # curent points for both players 0
    
    
    def startGame2p(self):
        currentScores = playr.getCurrentScore()
        score1 = currentScores[0]
        score2 = currentScores[1]
        while score1 != 100 and score2 != 100:
            self.ask_For_Rolls()
        else:
            winnerName = dise.getWinnerName()
            disp.winner(winnerName)
            whichPlayer = playr.getAmountOfRolls(winnerName)
            rollAmount = dise.amountOfRolls(whichPlayer)
            disp.gameSummary(winnerName, rollAmount)
            
    
    
    def enter_Names1(self):
        print("Existing players:")
        # need a view player list method
        name = input("Enter your name(note: if you already have your name in the list, enter it): ")
        # method of saving name if it's new
        # method of entering names into current player list with Ai
        # curent points for both 0

    
    def ask_For_Rolls(self):
        currentNames = playr.getCurrentNames()
        player1 = currentNames[0]
        player2 = currentNames[1]
        currentScores = playr.getCurrentScore()
        score1 = currentScores[0]
        score2 = currentScores[1]
        disp.viewGameProg2(player1, score1, player2, score2)
        print(currentPlayer,"\n")
        rollNum = input("Enter the number of dice-rolls you would like to do ('q' to quit, 'r' to restart): ")
        if rollNum.upper() == "Q":
            quit()
        elif rollNum.upper() == "CHEAT":
            self.cheat()
        elif rollNum.upper() == "R":
            self.restart()
        elif not isinstance(rollNum, int):
            print("You know that the number of rolls is a NUMBER right?")
        else:
            dise.roll(rollNum)
        if currentPlayer == "player1's turn":
            currentPlayer = "player2's turn"
        else:
            currentPlayer = "player1's turn"


    def ask_For_Rolls1p(self):
        
        
        print(currentPlayer1,"\n")
        roll_num = input("Enter the number of dice-rolls you would like to do ('q' to quit, 'r' to restart, 'cheat' to cheat): ")
        if roll_num.upper() == "Q":
            quit()
        elif roll_num.upper() == "CHEAT":
            self.cheat()
        elif roll_num.upper() == "R":
            self.restart()
        elif not isinstance(roll_num, int):
            print("You know that the number of rolls is a NUMBER right?")
        else:
            # call for the roll method (get back numbers)
            # if number returned == 1 break the rolls and bring current points to 0
            print("You rolled a 1 so your points for this turn are 0. Your current total points are: ")
            # else add number to current points
            print("You rolled a ", "Your total points are: ")
            # view roll number and points collected
            if currentPlayer1 == "player1's turn":
                currentPlayer1 = "AI's turn"
            else:
                currentPlayer1 = "player1's turn"


    def show_Ai_roll():
        print(currentPlayer1,"\n")
        # get the current name list
        # get the current point list
        # self.view_Game_Prog_2(name1, points1, name2, points2)
        # call for random roll amount (get back number)
        #loop
        # call for the roll method for the amount of times entered (get back numbers)
        if currentPlayer1 == "player1's turn":
            currentPlayer1 = "AI's turn"
        else:
            currentPlayer1 = "player1's turn"
    
    def cheat():
        #calculate difference from 100 returns amount of times to roll
        print("You just had to cheat, didn't you :(\nJust choose to roll {num} times")
        roll_num = input("Enter the number of dice-rolls you would like to do (q to quit, you already cheated!): ")
        #cheating method with 16 times rolling 6 and one time rolling 4
    
    
    def restart():
        # goes back to main menu
        pass
