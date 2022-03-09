from display import *
from game_functionality import *


gf = Game_functionality()
disp = Display()


def main():
    choice = disp.gameMenu()
    gf.handleMenuChoice(choice)


if __name__ == "__main__":
    main()
