"""
This script is used as a link to connect all classes to get a funtioning game.

Authors: Farah, Alfred, Emil
"""
from high_score import HighScore
from display import Display
from player import Player
from dice import Dice
from file_handling import FileHandling
from intelligence import Intelligence

hs = HighScore()
disp = Display()
playr = Player()
dise = Dice()
fh = FileHandling()
intel = Intelligence()


class GameFunctionality:
    """Connect all the other classes together to create a \
        functioning game."""

    current_player = "player1's turn"
    current_player1 = "player1's turn"
    difficulty = 0

    def handle_menu_choice(self, choice: int):
        """Take a choice: int as a parameter and depending on it \
            connect to the right methods."""
        if not isinstance(choice, int):
            raise ValueError("Please enter numbers only")

        if choice == 1:
            self.difficulty = disp.view_difficulties()
            if self.difficulty == 4:
                self.restart()
            self.enter_names1p()
            self.start_setup()
            self.start_game1p()
        elif choice == 2:
            self.enter_names2p()
            self.start_setup()
            self.start_game2p()
        elif choice == 3:
            names = fh.read_name_files("text_name_file.txt")
            disp.show_players(names)
            name = input("Enter the name you want to update: ")
            new_name = input("Enter the new updated name: ")
            playr.update_name(name, new_name)
            new_high_score = hs.update_high_score(name, new_name)
            fh.write_dic_files("text_high_score.txt", new_high_score)
            self.restart()
        elif choice == 4:
            names = fh.read_name_files("text_name_file.txt")
            disp.show_players(names)
            name = input("\nEnter the name you want to delete: ")
            playr.delete_name(name)
            self.restart()
        elif choice == 5:
            hs_dic = {}
            hs_dic = hs.get_high_score_dic()
            hs.view_high_scores(hs_dic)
            input(
                "\nWhen you are done reading the high scores press any \
                    button to go back: "
            )
            self.restart()
        elif choice == 6:
            disp.display_game_rules()
            input(
                "When you are done reading the rules press any button \
                to go back: "
            )
            self.restart()
        else:
            quit()

    def start_setup(self):
        """Do the necessary resetings of values before each game."""
        player_names = playr.get_current_names()
        disp.view_prog(player_names[0], 0, player_names[1], 0)
        dise.reset_totals()
        dise.reset_round_num()
        playr.reset_current_scores()

    def enter_names2p(self):
        """Ask for players names, add the names in the names list and the \
            current player list then save the names list in a txt file."""
        names = playr.get_names()
        disp.show_players(names)
        name = input(
            "Enter the name of player1(note: if you already have your name in \
                the list, enter it): "
        )
        name2 = input(
            "Enter the name of player2(note: if you already have your name in \
                the list, enter it): "
        )
        playr.set_name(name.capitalize())
        playr.set_name(name2.capitalize())
        names2 = playr.get_names()
        fh.write_name_files("text_name_file.txt", names2)
        playr.add_current_names(name, name2)

    def start_game2p(self):
        """Start the game for 2 players in a loop that would check if there \
            are winners so it can display the end screen."""
        score1 = dise.get_total_sum1()
        score2 = dise.get_total_sum2()
        while score1 < 100 and score2 < 100:
            self.ask_for_rolls()
            score1 = dise.get_total_sum1()
            score2 = dise.get_total_sum2()
        winner_name = dise.get_winner_name()
        disp.winner(winner_name)
        round_amount = dise.get_amount_of_rounds(winner_name)
        disp.game_summary(winner_name, round_amount)
        new_dic = hs.add_compare_high_scores(winner_name, round_amount)
        fh.write_dic_files("text_high_score.txt", new_dic)
        self.restart()

    def start_game1p(self):
        """Start the game for 1 player in a loop that would check if there \
            are winners so it can display the end screen."""
        score1 = dise.get_total_sum1()
        score2 = dise.get_total_sum2()
        while score1 < 100 and score2 < 100:
            self.ask_for_rolls1p()
            self.ai_roll()
            score1 = dise.get_total_sum1()
            score2 = dise.get_total_sum2()
        winner_name = dise.get_winner_name()
        disp.winner(winner_name)
        round_amount = dise.get_amount_of_rounds(winner_name)
        disp.game_summary(winner_name, round_amount)
        hs.add_compare_high_scores(winner_name, round_amount)
        self.restart()

    def enter_names1p(self):
        """Ask for the player name, add the name in the names list and the \
            current player list then save the names list in a txt file."""
        names = playr.get_names()
        disp.show_players(names)
        name = input(
            "Enter your name(note: if you already have your name in the list, \
                enter it): "
        )
        playr.set_name(name.capitalize())
        ai_name = intel.name_of_ai()
        names2 = playr.get_names()
        fh.write_name_files("text_name_file.txt", names2)
        playr.add_current_names(name, ai_name)

    def ask_for_rolls(self):
        """Ask the player for the number of rolls \
            handle the answer if it's a number \
            or in case it was a command, manipulate the game."""
        print(self.current_player, "\n")
        roll_num = input(
            "Enter the number of dice-rolls you would like to do ('q' to quit,\
                'r' to restart): "
        )
        if roll_num.upper() == "Q":
            quit()
        elif roll_num.upper() == "R":
            self.restart()
        elif roll_num.isdigit():
            introll_num = int(roll_num)
            dise.roll(introll_num)
            if self.current_player == "player1's turn":
                self.current_player = "player2's turn"
            else:
                self.current_player = "player1's turn"
        elif not isinstance(roll_num, int):
            print("\nYou know that the number of rolls is a NUMBER right?")

    def ask_for_rolls1p(self):
        """Ask the player for the number of rolls and \
            handle the answer if it's a number or in case it was a command,\
            manipulate the game."""
        roll_num = input(
            "Enter the number of dice-rolls you would like to do ('q' to quit,\
                'r' to restart, 'cheat' to cheat): "
        )
        if roll_num.upper() == "Q":
            quit()
        elif roll_num.upper() == "CHEAT":
            self.cheat()
        elif roll_num.upper() == "R":
            self.restart()
        elif roll_num.isdigit():
            introll_num = int(roll_num)
            dise.roll(introll_num)
        elif not isinstance(roll_num, int):
            print(
                "You know that the number of rolls is a positive NUMBER \
                right?"
            )

    def ai_roll(self):
        """Connect to the AI roll methods depending on the \
            dificulty choosen."""
        if self.difficulty == 1:
            roll_amount = intel.roll_amount_easy()
            print(f"Weird Ai Yankovic rolled {roll_amount} times\n")
            dise.easy_ai_roll(roll_amount)
        elif self.difficulty == 2:
            roll_amount = intel.roll_amount_nor_har()
            print(f"Weird Ai Yankovic rolled {roll_amount} times")
            dise.roll(roll_amount)
        elif self.difficulty == 3:
            roll_amount = intel.roll_amount_nor_har()
            print(f"Weird Ai Yankovic rolled {roll_amount} times")
            dise.hard_ai_roll(roll_amount)

    def cheat(self):
        """Change the score of the player in 99 as a cheat option."""
        dise.cheat_dice()
        print(
            "\nYou just had to cheat, didn't you :(\nAnyway, your score has \
                now been set to 99\n"
        )

    def restart(self):
        """Take you back to the main menu no matter where you are."""
        choice = disp.game_menu()
        self.handle_menu_choice(choice)
