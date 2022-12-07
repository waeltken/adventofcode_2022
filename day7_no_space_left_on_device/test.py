import unittest

from main import Folder, File, parse, read_input, folders_smaller_than

answer_one = 1989474

test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

test_file_tree = Folder(
    "",
    [
        Folder(
            "a",
            [
                Folder("e", [File("i", 584)]),
                File("f", 29116),
                File("g", 2557),
                File("h.lst", 62596),
            ],
        ),
        File("b.txt", 14848514),
        File("c.dat", 8504156),
        Folder(
            "d",
            [
                File("j", 4060174),
                File("d.log", 8033020),
                File("d.ext", 5626152),
                File("k", 7214296),
            ],
        ),
    ],
)


class TestParser(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(parse(""), Folder(""))

    def test_simple(self):
        self.assertEqual(
            parse(
                """$ cd /
$ ls
dir a
14848514 b.txt"""
            ),
            Folder("", [Folder("a"), File("b.txt", 14848514)]),
        )

    def test_sample(self):
        root = parse(test_input)
        self.assertEqual(root, test_file_tree)
        self.assertEqual(root.free_space, 21618835)

    def test_sum_of_small_folders(self):
        root = parse(read_input())
        sum_of_small_folders = sum([node.size for node in folders_smaller_than(root)])
        self.assertEqual(sum_of_small_folders, answer_one)


if __name__ == "__main__":
    unittest.main()
