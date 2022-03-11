"""
This tets the file handing class.

Authors: Farah, Alfred, Emil
"""
import unittest
from file_handling import FileHandling


fh = FileHandling()


class TestFileHandling(unittest.TestCase):
    """Testing the FileHandling class."""

    def test_read_name_files_wrong(self):
        """Testing the readNameFiles method \
Checking if a ValueError is raised."""
        with self.assertRaises(ValueError):
            fh.read_name_files(2)

#     def test_read_hs_file(self):
#         """Testing the readDicFiles method \
# Checking if a ValueError is raised."""
#         with self.assertRaises(ValueError):
#             fh.read_hs_file(3)

    def test_write_name_files(self):
        """Testing the writeNameFiles method \
Checking if a ValueError is raised."""
        with self.assertRaises(ValueError):
            fh.write_name_files("Pig/text_name_file.txt", 3)
        with self.assertRaises(ValueError):
            fh.write_name_files(8, [5, "Anna"])

    def test_write_hs_files(self):
        """Testing the writeDicFiles method \
Checking if a ValueError is raised."""
        with self.assertRaises(ValueError):
            fh.write_hs_files(4, [["Developer", 9001]])
        with self.assertRaises(ValueError):
            fh.write_hs_files("Pig/text_high_score.txt", 7)

    def test_write_hs_files_true(self):
        """Testing the writeDicFiles method \
Checking if a ValueError is raised."""
        self.assertTrue(fh.write_hs_files("Pig/text_high_score.txt",
                                          [["Developer", 9001]]), True)

    def test_write_name_files_true(self):
        """Testing the writeDicFiles method \
Checking if a ValueError is raised."""
        self.assertTrue(fh.write_name_files("Pig/text_name_file.txt",
                                            ["Kalle", "Peter"]), True)


if __name__ == "__main__":
    unittest.main()
