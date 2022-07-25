import unittest
from typing import List

from package_name.util.file import divide_file_path


class TestFile(unittest.TestCase):
    def test_file_path(self):
        test_cases: List[str] = [
            "./dir/subdir/filename.ext.ext2",
            "./dir/subdir/filename.ext",
            "./dir/subdir/filename",
            "./dir/filename.ext",
            "./dir/subdir/subdir2/filename.ext",
        ]
        answers_list: List[List[str]] = [
            ["./dir/subdir", "filename.ext.ext2", "subdir", "filename", "ext.ext2"],
            ["./dir/subdir", "filename.ext", "subdir", "filename", "ext"],
            ["./dir/subdir", "filename", "subdir", "filename", ""],
            ["./dir", "filename.ext", "dir", "filename", "ext"],
            ["./dir/subdir/subdir2", "filename.ext", "subdir2", "filename", "ext"],
        ]
        for (test_case, answers) in zip(test_cases, answers_list):
            dir_name, base_name, subdir_name, basename_without_ext, extension = divide_file_path(
                test_case
            )
            self.assertEqual(dir_name, answers[0])
            self.assertEqual(base_name, answers[1])
            self.assertEqual(subdir_name, answers[2])
            self.assertEqual(basename_without_ext, answers[3])
            self.assertEqual(extension, answers[4])
