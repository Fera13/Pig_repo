from file_handling import *

fh = File_handling()

class High_score:
    sorted_dict = fh.readDicFiles("high_score.txt")

    def __init__(self):
        pass


    def get_HighScore_Dic(self):
        return self.sorted_dict


    def view_HighScores(self, highScoreDic: dict[str: int]):
        i = 1
        print("High scores:\n")
        for keyName, valueScore in highScoreDic.items():
            print(f"{i}. {keyName:30} Score: {valueScore}")
            i += 1


    def update_High_Score(self, oldName: str, newName: str):
        if not isinstance(oldName, str) or not isinstance(newName, str):
            raise TypeError("The name should be a string and the score should be an integer")
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
        if not isinstance(name, str) or not isinstance(score, int):
            raise TypeError("The name should be a string and the score should be an integer")
        if len(self.sorted_dict.keys()) <= 5:
            self.sorted_dict[name] = score
            fh.writeDicFiles("high_score.txt", self.sorted_dict)
        else:
            sorted_tuples = sorted(self.sorted_dict.items(), key=lambda item: item[1], reverse=True)
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
        fh.writeDicFiles("high_score.txt", self.sorted_dict)
        return self.sorted_dict
