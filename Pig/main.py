from high_score import *
from display import *
from player import *
from dice import *
from main import *
from game_functionality import *


gf = Game_functionality()
hs = High_score()
disp = Display()
playr = Player()
dise = Dice()


def main():
    choice = disp.gameMenu()
    gf.handleMenuChoice(choice)


if __name__ == "__main__":
    main()
