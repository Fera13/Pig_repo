"""
This script is used to display the needed menues and options during the game.

Authors: Farah, Alfred, Emil
"""
from player import Player

playr = Player()


class Display:
    """Most of the interface in the game is in this class."""

    def winner(self, name: str):
        """Take a parameter: str, display who won the game."""
        if not isinstance(name, str):
            raise TypeError(
                "Something went wrong while trying to\
                    retrieve the winning players' name"
            )
        print("\n", "-" * 80)
        print(f"\n          Congratulations {name}, you have won the game!\n")
        print("-" * 80, "\n")

    def gameMenu(self):
        """Take no parameter, display the main menu, return the choice."""
        notCorrect = True
        while notCorrect:
            print("\n                           THE PIG GAME")
            print("-" * 70)
            print("1:  Start a one player game")
            print("2:  Start a two player game")
            print("3:  Update existing player name")
            print("4:  Delete existing player")
            print("5:  View highscore")
            print("6:  Show rules")
            print("7:  Exit game")
            print("-" * 70, "\n")
            choice = int(input("Please enter your choice here: "))
            if not isinstance(choice, int):
                raise ValueError(
                    "You can only use numbers\
                    to choose an option"
                )
            if choice in [1, 2, 3, 4, 5, 6, 7]:
                return choice
            print("Please enter a number from the available options")

    def displayGameRules(self):
        """Take no parameters, display the rules of the game."""
        print("\nThe rules for Pig-Game are as following:\n")
        print("-  The player begins each turn by rolling the dice.")
        print("-  The player may roll as many times as they want in a round.")
        print(
            "-  If the dice lands on a 1, the round ends and all \
                points from the current round will be deducted."
        )
        print(
            "-  For every other number on the dice the points relevant\
                to the dice surface will add up to a round total"
        )
        print("-  The first player to reach 100 points will be the victor!\n")

    def gameSummary(self, name: str, rounds: int):
        """Take parameters(name: str, amount of rounds: int), display a \
            summary of the winner and the amount of rounds."""
        if not isinstance(name, str) or not isinstance(rounds, int):
            raise TypeError("The game summary is not available right now")
        print(
            "\nHere is the amount of rolls for\
            the player to reach 100 points\n"
        )
        print(f'Name {"Amount of rounds":>35}')
        print("-" * 70)
        print(f"{name:25}  {rounds:>6}")
        print("-" * 70, "\n")

    def showPlayers(self, namelist: list[str]):
        """Take a parameter: list[str], show a list of all existing players."""
        length = 0
        amountOfNames = 0
        print("Here is the list of current players\n")
        print("-" * 70)
        while length < len(namelist):
            print("")
            while amountOfNames < 4 and length < len(namelist):
                print(f">{namelist[length]:15}", end=" ")
                length += 1
                amountOfNames += 1
            amountOfNames = 0
        print("\n\n")
        print("-" * 70)
        print("\n")

    def viewProg(self, player1: str, points1: int, player2: str, points2: int):
        """Take parameters(str, int, str, int) for names and points, show the \
            player names and how much points they currently have."""
        if (
            not isinstance(player1, str)
            or not isinstance(points1, int)
            or not isinstance(player2, str)
            or not isinstance(points2, int)
        ):
            raise TypeError("The game progress is not available right now")

        print(f"\n\nPlayer1: {player1:60} Player2: {player2}")
        print(f"Points: {points1:<61} Points: {points2}\n")

    def viewDifficulties(self):
        """Take no parameters, show the different difficulties of the AI,\
            return the choice."""
        notCorrect = True
        while notCorrect:
            print(
                "\nHere are the difficulties, which\
                one do you dare to oppose?\n"
            )
            print("1:  Easy Mode")
            print("2:  Normal Mode")
            print("3:  Hard Mode")
            print("4:  Go back to the main menu")
            choice = int(
                input(
                    "\nPlease enter the number of the challenge you\
                        dare to try today. It is okay to be a coward: "
                )
            )
            if not isinstance(choice, int):
                raise ValueError(
                    "You can only use numbers\
                    to choose an option"
                )
            if choice in [1, 2, 3, 4]:
                return choice
            print("Please enter a number from the available options")
