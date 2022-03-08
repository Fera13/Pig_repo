class Player:
    names = []
    score = []
    
    def __init__(self):
        return None

    def setName(self, name: str):
        if name in self.names:
            print(name + " has already been set")
        else:
            self.names.append(name)

        return len(self.names)

        # call method to update name in highscore
    

    def updateName(self, oldName:str, newName:str):
        if not isinstance(oldName,str) or not isinstance(newName,str):
            raise TypeError("oldName and newName has to be strings")

        for i in self.names:
            if i == oldName:
                self.deleteName(oldName)
                self.setName(newName)


    def deleteName(self, name: str):
        if not isinstance(name, str):
            raise TypeError("name has to be a string")
        for i in self.names:
            if i == name:
                self.names.remove(name)

    def addCurrentScore(self, score:int, name:str):
        if not isinstance(score, int) or not isinstance(name, str):
            raise TypeError("score has to be int and name has to be string")

        if score < 0:
            raise ValueError("score can be less than zero")

        if len(self.currentScores) < 2:
            self.currentScores.append([name, score])
        else:
            for i in range(2):
                if self.currentScores[i][0] == name:
                    self.currentScores[i][1] = score

    def getCurrentScore(self):
        return self.currentScores

    def addCurrentNames(self, name1: str, name2: str):
        if not isinstance(name1, str) or not isinstance(name2, str):
            raise TypeError("both names has to be string")
        self.currentNames.append(name1)
        self.currentNames.append(name2)

    def getCurrentNames(self):
        return self.currentNames

    def currentPlayers(self):
        return None
    def currentPlayer(self):
        return None


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

