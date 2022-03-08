class Player:
    names = []
    score = []
    currentNames = []
    
    def __init__(self):
        return None

    def setName(self, name: str):
        if name in self.names:
            print(name + " has already been set")
        else:
            self.names.append(name)

        return len(self.names)

        # call method to update name in highscore
    
    
    def addCurrentNames(self, name1: str, name2: str):
        self.currentNames.append(name1)
        self.currentNames.append(name2)
    
    
    def getCurrentNames(self):
        return self.currentNames
    
    
    def getNames(self):
        return self.names

    # not sure what for
    def setFinalScore(self, name: str, score: int):
        if not isinstance(name, str) or not isinstance(score, int):
            raise TypeError(
                "name has to be a string, and score has to be an integer")

        if score < 0:
            raise ValueError("score cant be a negative value")

        self.score.append([name, score])
        return self.score

    def getScore(self):
        return self.score
