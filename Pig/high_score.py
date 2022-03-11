"""
This script is used to create and update lists for the high scores.

Authors: Farah, Alfred, Emil
"""
from file_handling import FileHandling


fh = FileHandling()
high_score_list = fh.read_hs_file("Pig/text_high_score.txt")


class HighScore:
    """Do operation to compare, add, and update highscore."""

    def get_high_score_list(self):
        """Return the current high score list."""
        sorted_list = sorted(high_score_list, key=lambda x: x[1])
        return sorted_list

    def view_high_scores(self, high_score_list: list[list[str, int]]):
        """Take high score list: list[list] show high score."""
        if not isinstance(high_score_list, list):
            raise ValueError(
                "Please enter a list of lists with names and scores"
            )
        sorted_list = sorted(high_score_list, key=lambda x: x[1])
        order = 1
        ind = 0
        h = 0
        print("High scores:\n")
        while ind < len(sorted_list):
            name = sorted_list[h][0]
            score = sorted_list[h][1]
            ind += 1
            h += 1
            print(f"{order}. {name:30} Score: {score}")
            order += 1
        return True

    def update_high_score(self, old_name: str, new_name: str):
        """Take name, update old name to the new name in list."""
        if not isinstance(old_name, str) or not isinstance(new_name, str):
            raise ValueError(
                "The name should be a string and the score should be"
                "an integer"
            )
        for lis in high_score_list:
            for value in lis:
                if lis[0] == old_name:
                    lis[0] = new_name
        sorted_list = sorted(high_score_list, key=lambda x: x[1])
        return sorted_list

    def add_compare_high_scores(self, name: str, score: int):
        """Take name and score of winner, check if new high score."""
        if not isinstance(name, str) or not isinstance(score, int):
            raise ValueError(
                "The name should be a string and the score should be"
                "an integer"
            )
        if len(high_score_list) < 5:
            small_list = []
            small_list.append(name)
            small_list.append(score)
            high_score_list.append(small_list)
            sorted_list = sorted(high_score_list, key=lambda x: x[1])
            return sorted_list
        sorted_lis1 = sorted(high_score_list, key=lambda x: x[1], reverse=True)
        for lis in sorted_lis1:
            for value in lis:
                if lis[1] > score:
                    lis[0] = name
                    lis[1] = score
                break
            break
        sorted_list = sorted(sorted_lis1, key=lambda x: x[1])
        return sorted_list
