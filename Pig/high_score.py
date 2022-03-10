"""
This script is used to create and update dictionaries for high scores.

Authors: Farah, Alfred, Emil
"""
from file_handling import File_handling


fh = File_handling()


class High_score:
    """Do operation to compare, add, and update highscore."""

    sortedDic = fh.readDicFiles("text_high_score.txt")

    def get_HighScore_Dic(self):
        """Return the current high score dictionary."""
        return self.sortedDic

    def view_HighScores(self, highScoreDic: dict[str:int]):
        """Take high score dictionary and show high score on screen."""
        if not isinstance(highScoreDic, dict):
            raise ValueError(
                "Please enter a dictionary with strings as keys and integers \
                    as values!"
            )
        i = 1
        print("High scores:\n")
        for keyName, valueScore in highScoreDic.items():
            print(f"{i}. {keyName:30} Score: {valueScore}")
            i += 1

    def update_High_Score(self, oldName: str, newName: str):
        """Take name to update the old name to the new name \
            in the dictionary."""
        if not isinstance(oldName, str) or not isinstance(newName, str):
            raise ValueError(
                "The name should be a string and the score should be \
                an integer"
            )
        change = False
        for keyName in self.sortedDic.keys():
            if keyName == oldName:
                change = True
        if change is True:
            self.sortedDic[newName] = self.sortedDic.pop(oldName)
        sorted_tuples = \
            sorted(self.sortedDic.items(), key=lambda item: item[1])
        self.sortedDic = {k: v for k, v in sorted_tuples}
        return self.sortedDic

    def add_Compare_Highscores(self, name: str, score: int):
        """Take name and score of winner to check \
            if it is a new high score."""
        if not isinstance(name, str) or not isinstance(score, int):
            raise ValueError(
                "The name should be a string and the score should be \
                an integer"
            )
        if len(self.sortedDic.keys()) < 5:
            self.sortedDic[name] = score
        else:
            sorted_tuples = sorted(
                self.sortedDic.items(), key=lambda item: item[1], reverse=True
            )
            self.sortedDic = {k: v for k, v in sorted_tuples}
            for key, value in self.sortedDic.items():
                if name == key:
                    if value < score:
                        break
                    else:
                        self.sortedDic[name] = self.sortedDic.pop(key)
                        self.sortedDic[name] = score
                        break
                else:
                    if score < value:
                        self.sortedDic[name] = self.sortedDic.pop(key)
                        self.sortedDic[name] = score
                        break
        sorted_tuples = \
            sorted(self.sortedDic.items(), key=lambda item: item[1])
        self.sortedDic = {k: v for k, v in sorted_tuples}
        return self.sortedDic
