from High_score import *
from display import *
from player import *
from dice import *
from main import *
from Game_functionality import *

gf = Game_functionality()
hs = High_score()
disp = Display()
playr = Player()
dise = dice()


def main():
    choice = disp.gameMenu()
    gf.handleMenuChoice(choice)

# def handleMenuChoice(choice: int):
#     if choice == 1:
#         gf.enter_Names1()
#         # start game
#     elif choice == 2:
#         gf.enter_Names2p()
#         gf.startGame2p()
#     elif choice == 3:
#         names = playr.getNames()
#         disp.showPlayers(names)
#         name = input("Enter the name you want to update: ")
#         newName = input("Enter the new updated name: ")
#         playr.updateName(name, newName)
#         hs.update_High_Score(name, newName)
#     elif choice == 4:
#         names = playr.getNames()
#         disp.showPlayers(names)
#         name = input("\nEnter the name you want to delete: ")
#         playr.deleteName(name)
#     elif choice == 5:
#         hsDic = {}
#         hsDic = hs.get_HighScore_Dic()
#         hs.view_HighScores(hsDic)
#         back = input("\nWhen you are done reading the rules press and button to go back: ")
#         choice = disp.gameMenu()
#         handleMenuChoice(choice)
#     elif choice == 6:
#         disp.displayGameRules()
#         back = input("When you are done reading the rules press and button to go back: ")
#         choice = disp.gameMenu()
#         handleMenuChoice(choice)
#     else:
#         quit()
    
if __name__ == "__main__":
    main()
