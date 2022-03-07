from High_score import *
currentPlayer = "player1's turn"
currentPlayer1 = "player1's turn"

hs = High_score()

class Game_functionality:
    def view_Start_Menu():
        notCorrect = True
        while notCorrect:
            print("Welcome to Pig!\n")
            print("1. Start one player game\n2. Start two player game\n3. Update player name\n4. Delete player\n5. View highscores\n6. rules\n7. Exit\n")
            try:
                choice = input("Please enter a choice here: ")
                if choice in [1, 2, 3, 4, 5, 6, 7]:
                    return choice
                else:
                    print("Please enter a number from the available options")
            except TypeError:
                print("Please use numbers only")
    
    
    def handleMenuChoice(self, choice: int):
        if choice == 1:
            self.enter_Names1()
            # start game
        elif choice == 2:
            self.enter_Names2()
            # start game
        elif choice == 3:
            #view player list
            name = input("Enter the name you want to update: ")
            newName = input("Enter the new updated name: ")
            # method to switch names(name, newName)
        elif choice == 4:
            name = input("Enter the name you want to delete: ")
            #method of deleting a name from the list (name)
        elif choice == 5:
            hsDic = {}
            hsDic == hs.getHighScoreDic()
            hs.view_HighScores(hsDic)
        elif choice == 6:
            pass
        else:
            quit()
    
    
    def view_Game_Prog_2(player1: str, points1: int, player2: str, points2: int):
        print(f"Player1: {player1:60} Player2: {player2}")
        print(f"Points: {points1:<61} Points: {points2}\n")
    
    
    def enter_Names2(self):
        print("Existing players:")
        # need a view player list method
        name = input("Enter the name of player1(note: if you already have your name in the list, enter it): ")
        name2 = input("Enter the name of player2(note: if you already have your name in the list, enter it): ")
        # method of saving names if they are new
        # method of entering names into current player list
        # curent points for both players 0
    
    
    def enter_Names1(self):
        print("Existing players:")
        # need a view player list method
        name = input("Enter your name(note: if you already have your name in the list, enter it): ")
        # method of saving name if it's new
        # method of entering names into current player list with Ai
        # curent points for both 0

    
    def ask_For_Rolls(self):
        # get the current name list
        # get the current point list
        # self.view_Game_Prog_2(name1, points1, name2, points2)
        print(currentPlayer,"\n")
        roll_num = input("Enter the number of dice-rolls you would like to do (q to quit, cheat to cheat): ")
        # call for the roll method (get back numbers)
        if currentPlayer == "player1's turn":
            currentPlayer = "player2's turn"
        else:
            currentPlayer = "player1's turn"


    def ask_For_Rolls1p(self):
        # get the current name list
        # get the current point list
        # self.view_Game_Prog_2(name1, points1, name2, points2)
        print(currentPlayer1,"\n")
        roll_num = input("Enter the number of dice-rolls you would like to do (q to quit, cheat to cheat): ")
        if roll_num.upper() == "Q":
            quit()
        elif roll_num.upper() == "CHEAT":
            self.cheat()
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
        