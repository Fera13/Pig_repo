"""
This script is used to create and update dictionaries for high scores.

Authors: Farah, Alfred, Emil
"""
from file_handling import File_handling


fh = File_handling()


class High_score:
    """Do operation to compare, add, and update highscore."""

    sorted_dic = fh.readDicFiles("text_high_score.txt")

    def get_highScore_dic(self):
        """Return the current high score dictionary."""
        return self.sorted_dic

    def view_high_scores(self, high_score_dic: dict[str:int]):
        """Take high score dictionary and show high score on screen."""
        if not isinstance(high_score_dic, dict):
            raise ValueError(
                "Please enter a dictionary with strings as keys and integers \
                    as values!"
            )
        i = 1
        print("High scores:\n")
        for key_name, value_score in high_score_dic.items():
            print(f"{i}. {key_name:30} Score: {value_score}")
            i += 1

    def update_high_score(self, old_name: str, new_name: str):
        """Take name to update the old name to the new name \
            in the dictionary."""
        if not isinstance(old_name, str) or not isinstance(new_name, str):
            raise ValueError(
                "The name should be a string and the score should be \
                an integer"
            )
        change = False
        for key_name in self.sorted_dic.keys():
            if key_name == old_name:
                change = True
        if change is True:
            self.sortedDic[new_name] = self.sortedDic.pop(old_name)
        sorted_tuples =\
            sorted(self.sorted_dic.items(), key=lambda item: item[1])
        self.sortedDic = {k: v for k, v in sorted_tuples}
        return self.sorted_dic

    def add_compare_highscores(self, name: str, score: int):
        """Take name and score of winner to check \
            if it is a new high score."""
        if not isinstance(name, str) or not isinstance(score, int):
            raise ValueError(
                "The name should be a string and the score should be \
                an integer"
            )
        if len(self.sorted_dic.keys()) < 5:
            self.sorted_dic[name] = score
        else:
            sorted_tuples = sorted(
                self.sorted_dic.items(), key=lambda item: item[1], reverse=True
            )
            self.sorted_dic = {k: v for k, v in sorted_tuples}
            for key, value in self.sorted_dic.items():
                if name == key:
                    if value < score:
                        break
                    self.sorted_dic[name] = self.sorted_dic.pop(key)
                    self.sorted_dic[name] = score
                    break
                if score < value:
                    self.sorted_dic[name] = self.sorted_dic.pop(key)
                    self.sorted_dic[name] = score
                    break
        sorted_tuples = \
            sorted(self.sorted_dic.items(), key=lambda item: item[1])
        self.sorted_dic = {k: v for k, v in sorted_tuples}
        return self.sorted_dic
