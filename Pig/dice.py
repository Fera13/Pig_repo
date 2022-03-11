"""
This script is used to handle dice roll operations for a dice game.

Authors: Farah, Alfred, Emil
"""
from random import randrange, choice
from player import Player
from display import Display

player = Player()
dis = Display()


class Dice:
    """Do roll for player and AI, reset scores and return winner."""

    winner_name = ""
    amount_Of_rounds = [0, 0]
    scores = player.get_current_score()
    total_sum1 = scores[0]
    total_sum2 = scores[1]
    turn = 0
    score1 = 0
    score2 = 0

    def roll(self, times_to_roll: int):
        """Take one parameter: int, do roll for the times entered."""
        round_sum = 0
        if not isinstance(times_to_roll, int):
            raise TypeError("times_to_roll must be an integer")
        if times_to_roll <= 0:
            raise ValueError("times to roll has to be more than 0")
        names = player.get_current_names()
        i = 0
        while i < times_to_roll:
            roll_number = randrange(1, 7)
            if roll_number != 1:
                i += 1
                print("Rolled a " + str(roll_number))
                round_sum += roll_number
            else:
                round_sum = 0
                print(
                    "Rolled a 1, and therefore recieved 0 points \
this round"
                )
                break
        if self.turn == 0:
            self.total_sum1 += round_sum
            self.amount_Of_rounds[0] += 1
            self.turn = 1
            if self.total_sum1 >= 100:
                self.winner_name = names[0]
                self.turn = 0
            return round_sum
        else:
            self.total_sum2 += round_sum
            self.amount_Of_rounds[1] += 1
            self.turn = 0
            if self.total_sum2 >= 100:
                self.winner_name = names[1]
        dis.view_prog(names[0], self.total_sum1, names[1], self.total_sum2)
        return round_sum

    def hard_ai_roll(self, roll_num: int):
        """Take one parameter: int and roll for the AI."""
        if not isinstance(roll_num, int):
            raise TypeError("roll_num has be to an int")
        if roll_num <= 0:
            raise ValueError("roll_num has to be more than 0")
        round_sum = 0
        names = player.get_current_names()
        i = 0
        while i < roll_num:
            num = [1, 2, 3, 4, 4, 5, 5, 6, 6]
            roll_result = choice(num)
            if roll_result != 1:
                print("Rolled a " + str(roll_result))
                round_sum += roll_result
                i += 1
            else:
                round_sum = 0
                print(
                    "Even geniuses roll a 1, Weird Ai Yankovic got 0 points\
this round"
                )
                break
        self.total_sum2 += round_sum
        self.amount_Of_rounds[1] += 1
        self.turn = 0
        if self.total_sum2 >= 100:
            self.winner_name = names[1]
            self.turn = 0
        dis.view_prog(names[0], self.total_sum1, names[1], self.total_sum2)

    def easy_ai_roll(self, roll_num: int):
        """Take one parameter: int and roll for the AI."""
        if not isinstance(roll_num, int):
            raise TypeError("roll_num has be to an int")
        if roll_num <= 0:
            raise ValueError("roll_num has to be more than 0")
        round_sum = 0
        names = player.get_current_names()
        i = 0
        while i < roll_num:
            num = [1, 2, 3, 4, 5, 6, 1, 1]
            roll_result = choice(num)
            if roll_result != 1:
                print("Rolled a " + str(roll_result))
                round_sum += roll_result
                i += 1
            else:
                round_sum = 0
                print(
                    "Even geniuses roll a 1, Weird Ai Yankovic got 0 points\
this round"
                )
                break
        self.total_sum2 += round_sum
        self.amount_Of_rounds[1] += 1
        self.turn = 0
        if self.total_sum2 >= 100:
            self.winner_name = names[1]
            self.turn = 0
        dis.view_prog(names[0], self.total_sum1, names[1], self.total_sum2)

    def reset_totals(self):
        """Reset the total sum for both players."""
        self.total_sum1 = 0
        self.total_sum2 = 0
        return self.total_sum1

    def reset_round_num(self):
        """Reset the amount of rounds for both players."""
        self.amount_Of_rounds[0] = 0
        self.amount_Of_rounds[1] = 0
        return self.amount_Of_rounds[0]

    def get_winner_name(self):
        """Return the name of the winner."""
        return self.winner_name

    def get_total_sum1(self):
        """Return the total sum of the first player."""
        return self.total_sum1

    def get_total_sum2(self):
        """Return the total sum of the second player."""
        return self.total_sum2

    def get_amount_of_rounds(self, winner_name: str):
        """Take one parameter: str and return the amount of rounds."""
        names = player.get_current_names()
        if winner_name == names[0]:
            return self.amount_Of_rounds[0]
        return self.amount_Of_rounds[1]

    def cheat_dice(self):
        """Set the total sum of the first player to 99."""
        self.total_sum1 = 99
        return self.total_sum1
