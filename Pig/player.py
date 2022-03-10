from file_handling import *


fh = File_handling()


class Player:

    names = fh.readNameFiles("text_name_file.txt")
    currentNames = ["", ""]
    currentScores = [0, 0]

    def setName(self, name: str):
        '''Takes one parameter, name: str and sets the name'''
        if name in self.names:
            pass
        else:
            self.names.append(name)
        return len(self.names)

    def updateName(self, oldName: str, newName: str):
        '''Takes two parameters, oldName: str and newName: str and updates the name'''
        if not isinstance(oldName, str) or not isinstance(newName, str):
            raise TypeError("oldName and newName has to be strings")
        for index, item in enumerate(self.names):
            if item == oldName:
                self.names[index] = newName
        fh.writeNameFiles("text_name_file.txt", self.names)

    def deleteName(self, name: str):
        '''Takes one parameter, name: str and deletes the name'''
        if not isinstance(name, str):
            raise TypeError("name has to be a string")
        for i in self.names:
            if i == name:
                self.names.remove(name)
        fh.writeNameFiles("text_name_file.txt", self.names)

    def resetCurrentScores(self):
        '''Sets the current score to zero'''
        self.currentScores = [0, 0]

    def getCurrentScore(self):
        '''returns the current score'''
        return self.currentScores

    def addCurrentNames(self, name1: str, name2: str):
        '''Takes two parameters, name1: str and name2: str and adds them to list of names'''
        if not isinstance(name1, str) or not isinstance(name2, str):
            raise TypeError("both names has to be string")
        self.currentNames[0] = name1
        self.currentNames[1] = name2
        return self.currentNames[0]

    def getCurrentNames(self):
        '''returns a list of all current names'''
        return self.currentNames

    def getNames(self):
        '''return a list of all names'''
        return self.names
