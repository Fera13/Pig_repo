from high_score import *
from display import *
from player import *
from dice import *
from file_handling import *
from intelligence import *


hs = High_score()
disp = Display()
playr = Player()
dise = Dice()
fh = File_handling()
intel = Intelligence()


class Game_functionality:

    currentPlayer = "player1's turn"
    currentPlayer1 = "player1's turn"
    difficulty = 0

    def handleMenuChoice(self, choice: int):
        '''Takes a choice in the form of an integer and depending on it connects to the right methods'''
        if not isinstance(choice, int):
            raise ValueError("Please enter numbers only")

        if choice == 1:
            self.difficulty = disp.viewDifficulties()
            if self.difficulty == 4:
                self.restart()
            self.handleMenuChoice(choice)
            self.enter_Names1p()
            self.startSetup()
            self.startGame1p()
        elif choice == 2:
            self.enter_Names2p()
            self.startSetup()
            self.startGame2p()
        elif choice == 3:
            names = fh.readNameFiles("text_name_file.txt")
            disp.showPlayers(names)
            name = input("Enter the name you want to update: ")
            newName = input("Enter the new updated name: ")
            playr.updateName(name, newName)
            newHighScore = hs.update_High_Score(name, newName)
            fh.writeDicFiles("text_high_score.txt", newHighScore)
            self.restart()
        elif choice == 4:
            names = fh.readNameFiles("text_name_file.txt")
            disp.showPlayers(names)
            name = input("\nEnter the name you want to delete: ")
            playr.deleteName(name)
            self.restart()
        elif choice == 5:
            hsDic = {}
            hsDic = hs.get_HighScore_Dic()
            hs.view_HighScores(hsDic)
            input(
                "\nWhen you are done reading the high scores press any button to go back: "
            )
            self.restart()
        elif choice == 6:
            disp.displayGameRules()
            input("When you are done reading the rules press any button to go back: ")
            self.restart()
        else:
            quit()

    def startSetup(self):
        '''Does the necessary resetings of values before each game'''
        playerNames = playr.getCurrentNames()
        disp.viewGameProg2(playerNames[0], 0, playerNames[1], 0)
        dise.resetTotals()
        dise.resetRoundNum()
        playr.resetCurrentScores()

    def enter_Names2p(self):
        '''Asks for players' names, adds the names in the names list and the current player list then saves the names list in a txt file'''
        names = playr.getNames()
        disp.showPlayers(names)
        name = input(
            "Enter the name of player1(note: if you already have your name in the list, enter it): "
        )
        name2 = input(
            "Enter the name of player2(note: if you already have your name in the list, enter it): "
        )
        playr.setName(name.capitalize())
        playr.setName(name2.capitalize())
        names2 = playr.getNames()
        fh.writeNameFiles("text_name_file.txt", names2)
        playr.addCurrentNames(name, name2)

    def startGame2p(self):
        '''Starts the game for 2 players in a loop that would check if there are winners so it can display the end screen'''
        score1 = dise.getTotalSum1()
        score2 = dise.getTotalSum2()
        while score1 < 100 and score2 < 100:
            self.ask_For_Rolls()
            score1 = dise.getTotalSum1()
            score2 = dise.getTotalSum2()
        else:
            winnerName = dise.getWinnerName()
            disp.winner(winnerName)
            roundAmount = dise.getAmountOfRounds(winnerName)
            disp.gameSummary(winnerName, roundAmount)
            newDic = hs.add_Compare_Highscores(winnerName, roundAmount)
            fh.writeDicFiles("text_high_score.txt", newDic)
            self.restart()

    def startGame1p(self):
        '''Starts the game for 1 players in a loop that would check if there are winners so it can display the end screen'''
        score1 = dise.getTotalSum1()
        score2 = dise.getTotalSum2()
        while score1 < 100 and score2 < 100:
            self.ask_For_Rolls1p()
            self.aiRoll()
            score1 = dise.getTotalSum1()
            score2 = dise.getTotalSum2()
        else:
            winnerName = dise.getWinnerName()
            disp.winner(winnerName)
            roundAmount = dise.getAmountOfRounds(winnerName)
            disp.gameSummary(winnerName, roundAmount)
            hs.add_Compare_Highscores(winnerName, roundAmount)
            self.restart()

    def enter_Names1p(self):
        '''Asks for the player name, adds the name in the names list and the current player list then saves the names list in a txt file'''
        names = playr.getNames()
        disp.showPlayers(names)
        name = input(
            "Enter your name(note: if you already have your name in the list, enter it): "
        )
        playr.setName(name.capitalize())
        aiName = intel.nameOfAi()
        names2 = playr.getNames()
        fh.writeNameFiles("text_name_file.txt", names2)
        playr.addCurrentNames(name, aiName)

    def ask_For_Rolls(self):
        '''Asks the player for the number of rolls he wants and handles the answer if it's a number or in case it was a command to manipulate the game'''
        print(self.currentPlayer, "\n")
        rollNum = input(
            "Enter the number of dice-rolls you would like to do ('q' to quit, 'r' to restart): "
        )
        if rollNum.upper() == "Q":
            quit()
        elif rollNum.upper() == "R":
            self.restart()
        elif rollNum.isdigit():
            intRollNum = int(rollNum)
            dise.roll(intRollNum)
            if self.currentPlayer == "player1's turn":
                self.currentPlayer = "player2's turn"
            else:
                self.currentPlayer = "player1's turn"
        elif not isinstance(rollNum, int):
            print("\nYou know that the number of rolls is a NUMBER right?")

    def ask_For_Rolls1p(self):
        '''Asks the player for the number of rolls he wants and handles the answer if it's a number or in case it was a command to manipulate the game'''
        rollNum = input(
            "Enter the number of dice-rolls you would like to do ('q' to quit, 'r' to restart, 'cheat' to cheat): "
        )
        if rollNum.upper() == "Q":
            quit()
        elif rollNum.upper() == "CHEAT":
            self.cheat()
        elif rollNum.upper() == "R":
            self.restart()
        elif rollNum.isdigit():
            intRollNum = int(rollNum)
            dise.roll(intRollNum)
        elif not isinstance(rollNum, int):
            print("You know that the number of rolls is a positive NUMBER right?")

    def aiRoll(self):
        '''Connects to the AI roll methods depending on the dificulty choosen'''
        if self.difficulty == 1:
            rollAmount = intel.rollAmountEasy()
            print(f"Weird Ai Yankovic rolled {rollAmount} times\n")
            dise.easyAiRoll(rollAmount)
        elif self.difficulty == 2:
            rollAmount = intel.rollAmountNorHar()
            print(f"Weird Ai Yankovic rolled {rollAmount} times")
            dise.roll(rollAmount)
        elif self.difficulty == 3:
            rollAmount = intel.rollAmountNorHar()
            print(f"Weird Ai Yankovic rolled {rollAmount} times")
            dise.hardAiRoll(rollAmount)

    def cheat(self):
        '''Changes the score of the player in 99 as a cheat option'''
        dise.cheatDice()
        print(
            "\nYou just had to cheat, didn't you :(\nAnyway, your score has now been set to 99\n"
        )

    def restart(self):
        '''Gets you back to the main menu no matter where you are'''
        choice = disp.gameMenu()
        self.handleMenuChoice(choice)
