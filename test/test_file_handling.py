"""
This tets the file handing class.

Authors: Farah, Alfred, Emil
"""
import unittest
from file_handling import FileHandling


fh = FileHandling()


class TestFileHandling(unittest.TestCase):
    """Testing the FileHandling class."""

    def test_read_name_files(self):
        """Testing the readNameFiles method\
        Checking if a ValueError is raised."""
        with self.assertRaises(ValueError):
            fh.read_name_files(2)

    def test_read_dic_files(self):
        """Testing the readDicFiles method\
        Checking if a ValueError is raised."""
        with self.assertRaises(ValueError):
            fh.read_dic_files(3)

    def test_write_name_files(self):
        """Testing the writeNameFiles method\
        Checking if a ValueError is raised."""
        with self.assertRaises(ValueError):
            fh.write_name_files("Pig/text_name_file.txt", 3)
        with self.assertRaises(ValueError):
            fh.write_name_files(8, ["Kalle", "Anna"])

    def test_write_dic_files(self):
        """Testing the writeDicFiles method\
        Checking if a ValueError is raised."""
        with self.assertRaises(ValueError):
            fh.write_dic_files(4, {"Kalle": 7})
        with self.assertRaises(ValueError):
            fh.write_dic_files("Pig/text_name_file.txt", 7)


if __name__ == "__main__":
    unittest.main()
