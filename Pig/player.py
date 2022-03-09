from file_handling import *

fh = File_handling()

class Player:
    names = fh.readNameFiles("name_file.txt")
    currentNames = ["", ""]
    currentScores = [ 0, 0]

    def __init__(self):
        return None


    def setName(self, name: str):
        if name in self.names:
            print(name + " has already been set")
        else:
            self.names.append(name)
        return len(self.names)

        # call method to update name in highscore


    def updateName(self, oldName: str, newName: str):
        if not isinstance(oldName, str) or not isinstance(newName, str):
            raise TypeError("oldName and newName has to be strings")
        for index, item in enumerate(self.names):
            if item == oldName:
                self.names[index] = newName
        fh.writeNameFiles("name_file.txt", self.names)
        self.names = fh.readNameFiles("name_file.txt")


    def deleteName(self, name: str):
        if not isinstance(name, str):
            raise TypeError("name has to be a string")
        for i in self.names:
            if i == name:
                self.names.remove(name)


    def addCurrentScore(self, score: int, name: str):
        if not isinstance(score, int) or not isinstance(name, str):
            raise TypeError("score has to be int and name has to be string")

        if score < 0:
            raise ValueError("score can be less than zero")
        if name == self.currentNames[0]:
            self.currentScores[0] = score
        else:
            self.currentScores[1] = score


    def resetCurrentScores(self):
        self.currentScores = [ 0, 0]


    def getCurrentScore(self):
        return self.currentScores


    def addCurrentNames(self, name1: str, name2: str):
        if not isinstance(name1, str) or not isinstance(name2, str):
            raise TypeError("both names has to be string")
        self.currentNames[0] = name1
        self.currentNames[1] = name2


    def getCurrentNames(self):
        return self.currentNames


    def currentPlayers(self):
        return None


    def currentPlayer(self):
        return None


    def getNames(self):
        return self.names


    # def getAmountOfRolls(self, winnerName: str):
    #     if self.currentNames[0] == winnerName:
    #         num = 0
    #         return num
    #     else:
    #         return 1


    def getScore(self):
        return self.score
