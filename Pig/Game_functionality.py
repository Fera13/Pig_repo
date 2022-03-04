from High_score import *
currentPlayer = "player1's turn"

class Game_functionality:
    def view_Start_Menu():
        notCorrect = True
        while notCorrect:
            print("Welcome to Pig!\n")
            print("1. Start one player game\n2. Start two player game\n3. Update player name\n4. Delete player\n5. View highscores\n6. Exit\n")
            try:
                choice = input("Please enter a choice here: ")
                if choice in [1, 2, 3, 4, 5, 6]:
                    return choice
                else:
                    print("Please enter a number from the available options")
            except TypeError:
                print("Please use numbers only")
    
    
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
        
    
    def ask_For_Rolls():
        # use my view_game_prog 
        print(currentPlayer,"\n")
        roll_num = input("Enter the number of dice-rolls you would like to do (enter 0 if you don't want to roll): ")
        #loop amount of rolls
        # call for the roll method (get back numbers)
        # if number returned == 1 break the rolls and bring current points to 0
        print("You rolled a 1 so your points for this turn are 0. Your current total points are: ")
        # else add number to current points
        print("You rolled a ", "Your total points are: ")
        # view roll number and points collected
        if currentPlayer == "player1's turn":
            currentPlayer = "player2's turn"
        else:
            currentPlayer = "player1's turn"
            
    
    def show_Ai_roll():
        # call for random roll amount (get back number)
        #loop
        # call for the roll method for the amount of times entered (get back numbers)
        # if number returned == 1 break the rolls and bring current points to 0
        print("The AI rolled a 1 so it gets 0 points for this turn. AI's current total points are: ")
        # else add number to current points
        print("The AI rolled a ", "AI's total points are: ")
        if currentPlayer == "player1's turn":
            currentPlayer = "AI's turn"
        else:
            currentPlayer = "player1's turn"
        