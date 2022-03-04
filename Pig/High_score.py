

highScoreDic = {}
class High_score:
    
    def __init__(self):
        pass


    def view_HighScores(highScoreDic: dict[str: int]):
        if not isinstance(highScoreDic, dict[str: int]):
             raise TypeError("Please enter a dictionary with strings as keys and integers as values")
        i = 1
        print("High scores:\n")
        for keyName, valueScore in highScoreDic.items():
            print(f"{i}. {keyName:30} Score: {valueScore}")
            i += 1


    def add_Compare_Highscores(name: str, score: int):
        if not isinstance(name, str) or not isinstance(score, int):
            raise TypeError("The name should be a string and the score should be an integer")
        if len(highScoreDic.keys()) < 5:
            highScoreDic[name] = score
            sorted_tuples = sorted(highScoreDic.items(), key=lambda item: item[1], reverse=True)
            sorted_dict = {k: v for k, v in sorted_tuples}
        else:
            sorted_tuples = sorted(highScoreDic.items(), key=lambda item: item[1], reverse=True)
            sorted_dict = {k: v for k, v in sorted_tuples}
            for keyName, valueScore in sorted_dict.items():
                if score < valueScore:
                    sorted_dict[name] = sorted_dict.pop(keyName)
                    sorted_dict[name] = score
                    break
        sorted_tuples = sorted(sorted_dict.items(), key=lambda item: item[1])  
        sorted_dict = {k: v for k, v in sorted_tuples}
        return sorted_dict

    
    