"""
This script is to read, write text files to get/save highscores and names.

Authors: Farah, Alfred, Emil
"""


class File_handling:
    """Class for handling all files."""

    def readNameFiles(self, filename: str):
        """Take a file as parameter: str, read the contents from the file,\
            return a list with the content."""
        names = []
        if not isinstance(filename, str):
            raise ValueError("The file was not correct")
        reading = open(filename, "r", encoding="utf8")
        for line in reading:
            name = line.rstrip("\n")
            names.append((name))
        reading.close()
        return names

    def writeNameFiles(self, filename: str, names: list[str]):
        """Take a file: str and a list: list[str] as parameters, write the\
            content in the list to the file, close the file."""
        if not isinstance(filename, str) or not isinstance(names, list):
            raise ValueError("The file or the list was not correct")
        writing = open(filename, "w", encoding="utf8")
        for name in names:
            writing.write(name + "\n")
        writing.close()

    def readDicFiles(self, filename: str):
        """Take a file as a parameter: str, read the content from the file,\
            return a dictionary with the content."""
        highScoreDic = {}
        name = ""
        score = 0
        if not isinstance(filename, str):
            raise ValueError("The file was not correct")
        reading = open(filename, "r", encoding="utf8")
        for line in reading:
            name = line.rstrip("\n")
            score = reading.readline().rstrip("\n")
            intValue = int(score)
            highScoreDic[name] = intValue
        reading.close()
        return highScoreDic

    def writeDicFiles(self, filename: str, highScoreDic: dict[str:int]):
        """Take a file: str and a dictionary: dict[str: int] as parameters,\
            write the content in the dictionary to the file, close the file."""
        if not isinstance(filename, str) or not isinstance(highScoreDic, dict):
            raise ValueError("The file or the dictionary was not correct")
        writing = open(filename, "w", encoding="utf8")
        for key, value in highScoreDic.items():
            stringvalue = str(value)
            writing.write(key + "\n" + stringvalue + "\n")
        writing.close()
