import unittest
from file_handling import *


fh = File_handling()


class TestFileHandling(unittest.TestCase):
    def test_read_name_files(self):
        with self.assertRaises(ValueError):
            fh.readNameFiles(2)

    def test_read_dic_files(self):
        with self.assertRaises(ValueError):
            fh.readDicFiles(3)

    def test_write_name_files(self):
        with self.assertRaises(ValueError):
            fh.writeNameFiles("text_name_file.txt", 3)
        with self.assertRaises(ValueError):
            fh.writeNameFiles(8, ["Kalle", "Anna"])

    def test_write_dic_files(self):
        with self.assertRaises(ValueError):
            fh.writeDicFiles(4, {"Kalle": 7})
        with self.assertRaises(ValueError):
            fh.writeDicFiles("text_name_file.txt", 7)


if __name__ == "__main__":
    unittest.main()
