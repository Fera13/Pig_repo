"""
This script is used to create lists for handling players and update list.

Authors: Farah, Alfred, Emil
"""
from file_handling import FileHandling


fh = FileHandling()


class Player:
    """This class represents the players. it is responsible for updating, \
        settting, and deleting names, and also setting scores."""

    names = fh.read_name_files("text_name_file.txt")
    current_names = ["", ""]
    current_scores = [0, 0]

    def set_name(self, name: str):
        """Take one parameter, name: str and set the name."""
        if name in self.names:
            pass
        else:
            self.names.append(name)
        return len(self.names)

    def update_name(self, old_name: str, new_name: str):
        """Take two parameters, old_name: str and new_name: str and update \
            the name."""
        if not isinstance(old_name, str) or not isinstance(new_name, str):
            raise TypeError("old_name and new_name has to be strings")
        for index, item in enumerate(self.names):
            if item == old_name:
                self.names[index] = new_name
        fh.write_name_files("text_name_file.txt", self.names)

    def delete_name(self, name: str):
        """Take one parameter, name: str and delete the name."""
        if not isinstance(name, str):
            raise TypeError("name has to be a string")
        for i in self.names:
            if i == name:
                self.names.remove(name)
        fh.write_name_files("text_name_file.txt", self.names)

    def reset_current_scores(self):
        """Set current score to zero."""
        self.current_scores = [0, 0]

    def get_current_score(self):
        """Return current score."""
        return self.current_scores

    def add_current_names(self, name1: str, name2: str):
        """Take two parameters, name1: str and name2: str and add them to \
            list of names."""
        if not isinstance(name1, str) or not isinstance(name2, str):
            raise TypeError("both names has to be string")
        self.current_names[0] = name1
        self.current_names[1] = name2
        return self.current_names[0]

    def get_current_names(self):
        """Return a list of all current names."""
        return self.current_names

    def get_names(self):
        """Return a list of all names."""
        return self.names
