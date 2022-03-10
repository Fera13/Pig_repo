from typing import Dict
from file_handling import *


fh = File_handling()


class High_score:

    sorted_dict = fh.readDicFiles("text_high_score.txt")

    def get_HighScore_Dic(self):
        '''Returns the current high score dictionary'''
        return self.sorted_dict

    def view_HighScores(self, highScoreDic: dict[str:int]):
        '''Takes a high score dictionary and iterates through it, showing the high scores on the screen'''
        if not isinstance(highScoreDic, dict):
            raise ValueError(
                "Please enter a dictionary with strings as keys and integers as values!"
            )
        i = 1
        print("High scores:\n")
        for keyName, valueScore in highScoreDic.items():
            print(f"{i}. {keyName:30} Score: {valueScore}")
            i += 1

    def update_High_Score(self, oldName: str, newName: str):
        '''Takes the name that needs to be updated as well as the new name (2 strings) then iterates through the high score dictionary to update the old name'''
        if not isinstance(oldName, str) or not isinstance(newName, str):
            raise ValueError(
                "The name should be a string and the score should be an integer"
            )
        change = False
        for keyName in self.sorted_dict.keys():
            if keyName == oldName:
                change = True
        if change == True:
            self.sorted_dict[newName] = self.sorted_dict.pop(oldName)
        sorted_tuples = sorted(self.sorted_dict.items(), key=lambda item: item[1])
        self.sorted_dict = {k: v for k, v in sorted_tuples}
        return self.sorted_dict

    def add_Compare_Highscores(self, name: str, score: int):
        '''Takes the name and the score of the winner (string, int) then iterates through the high score dictionary to enter the new name/score if it breaks the old scores'''
        if not isinstance(name, str) or not isinstance(score, int):
            raise ValueError(
                "The name should be a string and the score should be an integer"
            )
        if len(self.sorted_dict.keys()) < 5:
            self.sorted_dict[name] = score
        else:
            sorted_tuples = sorted(
                self.sorted_dict.items(), key=lambda item: item[1], reverse=True
            )
            self.sorted_dict = {k: v for k, v in sorted_tuples}
            for key, value in self.sorted_dict.items():
                if name == key:
                    if value < score:
                        break
                    else:
                        self.sorted_dict[name] = self.sorted_dict.pop(key)
                        self.sorted_dict[name] = score
                        break
                else:
                    if score < value:
                        self.sorted_dict[name] = self.sorted_dict.pop(key)
                        self.sorted_dict[name] = score
                        break
        sorted_tuples = sorted(self.sorted_dict.items(), key=lambda item: item[1])
        self.sorted_dict = {k: v for k, v in sorted_tuples}
        return self.sorted_dict
