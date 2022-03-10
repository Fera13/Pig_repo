"""
This script is used to create lists for handling players and update list.

Authors: Farah, Alfred, Emil
"""
from file_handling import File_handling


fh = File_handling()


class Player:
    """This class represents the players. it is responsible for updating, \
        settting, and deleting names, and also setting scores."""

    names = fh.readNameFiles("text_name_file.txt")
    currentNames = ["", ""]
    currentScores = [0, 0]

    def setName(self, name: str):
        """Take one parameter, name: str and set the name."""
        if name in self.names:
            pass
        else:
            self.names.append(name)
        return len(self.names)

    def updateName(self, oldName: str, newName: str):
        """Take two parameters, oldName: str and newName: str and update \
            the name."""
        if not isinstance(oldName, str) or not isinstance(newName, str):
            raise TypeError("oldName and newName has to be strings")
        for index, item in enumerate(self.names):
            if item == oldName:
                self.names[index] = newName
        fh.writeNameFiles("text_name_file.txt", self.names)

    def deleteName(self, name: str):
        """Take one parameter, name: str and delete the name."""
        if not isinstance(name, str):
            raise TypeError("name has to be a string")
        for i in self.names:
            if i == name:
                self.names.remove(name)
        fh.writeNameFiles("text_name_file.txt", self.names)

    def resetCurrentScores(self):
        """Set current score to zero."""
        self.currentScores = [0, 0]

    def getCurrentScore(self):
        """Return current score."""
        return self.currentScores

    def addCurrentNames(self, name1: str, name2: str):
        """Take two parameters, name1: str and name2: str and add them to \
            list of names."""
        if not isinstance(name1, str) or not isinstance(name2, str):
            raise TypeError("both names has to be string")
        self.currentNames[0] = name1
        self.currentNames[1] = name2
        return self.currentNames[0]

    def getCurrentNames(self):
        """Return a list of all current names."""
        return self.currentNames

    def getNames(self):
        """Return a list of all names."""
        return self.names
