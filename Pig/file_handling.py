"""
This script is to read, write text files to get/save highscores and names.

Authors: Farah, Alfred, Emil
"""


class FileHandling:
    """Class for handling all files."""

    def read_name_files(self, file_name: str):
        """Take a file as parameter: str, read the contents from the file,\
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

    def read_hs_file(self, file_name: str):
        """Take a file as parameter: str, read the contents from the file,\
            return a list with the content."""
        reading = open(file_name, "r", encoding="utf8")
        high_scores = []
        for line in reading:
            small_list = []
            name = line.rstrip("\n")
            small_list.append(name)
            score = reading.readline().rstrip("\n")
            small_list.append(int(score))
            high_scores.append(small_list)
            return high_scores

    def write_hs_files(self, file_name: str,
                       high_scores: list[list[str, int]]):
        """Take a file: str and a list: list[list[str: int]] as parameters,\
            write the content in the list to the file, close the file."""
        if not isinstance(file_name, str) or not isinstance(high_scores, list):
            raise ValueError("The file or the list was not correct")
        writing = open(file_name, "w", encoding="utf8")
        for lis in high_scores:
            for value in lis:
                writing.write(str(value) + "\n")
        writing.close()
        return True

    def write_name_files(self, file_name: str, names: list[str]):
        """Take a file: str and a list: list[str] as parameters, write the\
            content in the list to the file, close the file."""
        if not isinstance(file_name, str) or not isinstance(names, list):
            raise ValueError("The file or the list was not correct")
        writing = open(file_name, "w", encoding="utf8")
        for name in names:
            writing.write(name + "\n")
        writing.close()
        return True
