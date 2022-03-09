import unittest
from file_handling import *


fh = File_handling()


class TestFileHandling(unittest.TestCase):


    def test_read_name_files(self):
        with self.assertRaises(ValueError): fh.readNameFiles(2)


    def test_read_dic_files(self):
        with self.assertRaises(ValueError): fh.readDicFiles(3)


    def test_write_name_files(self):
        with self.assertRaises(ValueError): fh.writeNameFiles(3, [3,4,5])


    def test_write_dic_files(self):
        with self.assertRaises(ValueError): fh.writeDicFiles(4, {3,""})


if __name__ == '__main__':
    unittest.main()