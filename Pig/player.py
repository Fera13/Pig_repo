from file_handling import *


fh = File_handling()


class Player:

    names = fh.readNameFiles("text_name_file.txt")
    currentNames = ["", ""]
    currentScores = [0, 0]

    def setName(self, name: str):
        if name in self.names:
            pass
        else:
            self.names.append(name)
        return len(self.names)

    def updateName(self, oldName: str, newName: str):
        if not isinstance(oldName, str) or not isinstance(newName, str):
            raise TypeError("oldName and newName has to be strings")
        for index, item in enumerate(self.names):
            if item == oldName:
                self.names[index] = newName
        fh.writeNameFiles("text_name_file.txt", self.names)

    def deleteName(self, name: str):
        if not isinstance(name, str):
            raise TypeError("name has to be a string")
        for i in self.names:
            if i == name:
                self.names.remove(name)
        fh.writeNameFiles("text_name_file.txt", self.names)

    def resetCurrentScores(self):
        self.currentScores = [0, 0]

    def getCurrentScore(self):
        return self.currentScores

    def addCurrentNames(self, name1: str, name2: str):
        if not isinstance(name1, str) or not isinstance(name2, str):
            raise TypeError("both names has to be string")
        self.currentNames[0] = name1
        self.currentNames[1] = name2
        return self.currentNames[0]

    def getCurrentNames(self):
        return self.currentNames

    def getNames(self):
        return self.names
