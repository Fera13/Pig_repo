"""
This script is to read, write text files to get/save highscores and names.

Authors: Farah, Alfred, Emil
"""


class FileHandling:
    """Class for handling all files."""

    def read_name_files(self, file_name: str):
        """Take a file as parameter: str, read the contents from the file, \
return a list with the content."""
        names = []
        if not isinstance(file_name, str):
            raise ValueError("The file was not correct")
        reading = open(file_name, "r", encoding="utf8")
        for line in reading:
            name = line.rstrip("\n")
            names.append((name))
        reading.close()
        return names

    def write_name_files(self, file_name: str, names: list[str]):
        """Take a file: str and a list: list[str] as parameters, write the \
content in the list to the file, close the file."""
        if not isinstance(file_name, str) or not isinstance(names, list):
            raise ValueError("The file or the list was not correct")
        writing = open(file_name, "w", encoding="utf8")
        for name in names:
            writing.write(name + "\n")
        writing.close()

    def read_dic_files(self, file_name: str):
        """Take a file as a parameter: str, read the content from the file, \
return a dictionary with the content."""
        highscore_dic = {}
        name = ""
        score = 0
        if not isinstance(file_name, str):
            raise ValueError("The file was not correct")
        reading = open(file_name, "r", encoding="utf8")
        for line in reading:
            name = line.rstrip("\n")
            score = reading.readline().rstrip("\n")
            int_value = int(score)
            highscore_dic[name] = int_value
        reading.close()
        return highscore_dic

    def write_dic_files(self, file_name: str, highscore_dic: dict[str:int]):
        """Take a file: str and a dictionary: dict[str: int] as parameters, \
write the content in the dictionary to the file, close the file."""
        if not isinstance(file_name, str)\
           or not isinstance(highscore_dic, dict):
            raise ValueError("The file or the dictionary was not correct")
        writing = open(file_name, "w", encoding="utf8")
        for key, value in highscore_dic.items():
            string_value = str(value)
            writing.write(key + "\n" + string_value + "\n")
        writing.close()
