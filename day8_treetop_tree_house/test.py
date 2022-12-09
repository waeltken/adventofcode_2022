import unittest

from main import Wood, read_input

test_input = """30373
25512
65332
33549
35390"""


class TestSimple(unittest.TestCase):
    def setUp(self):
        self.wood = Wood(test_input.splitlines())

    def test_constructor(self):
        self.assertEquals(
            self.wood.map,
            [
                [3, 0, 3, 7, 3],
                [2, 5, 5, 1, 2],
                [6, 5, 3, 3, 2],
                [3, 3, 5, 4, 9],
                [3, 5, 3, 9, 0],
            ],
        )

    def test_trees_visible(self):
        should_be_visible = {
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (4, 1),
            (4, 2),
            (4, 3),
            (4, 4),
            (3, 4),
            (2, 4),
            (1, 4),
            (0, 4),
            (0, 3),
            (0, 2),
            (0, 1),
            (0, 0),
            (1, 1),  # Top left 5
            (1, 2),  # Top middle 5
            (2, 1),  # Left middle 5
            (2, 3),  # Right middle 3
            (3, 2),  # Bottom middle 5
        }
        visible = self.wood.visible_trees()
        self.assertEquals(visible, should_be_visible)
        self.assertEquals(len(visible), 21)

    def test_sceenic_score(self):
        self.assertEquals(self.wood.scenic_score((1, 2)), 4)
        self.assertEquals(self.wood.scenic_score((3, 2)), 8)
        self.assertEquals(self.wood.max_scenic_score(), 8)


class TestInput(unittest.TestCase):
    def setUp(self) -> None:
        self.wood = Wood(read_input())

    def test_visible_trees(self):
        self.assertEquals(len(self.wood.visible_trees()), 1776)

    def test_max_scenic_score(self):
        self.assertEquals(self.wood.max_scenic_score(), 234416)


if __name__ == "__main__":
    unittest.main()
