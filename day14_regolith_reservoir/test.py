import unittest

from main import Cave

sample_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


def read_input():
    with open("day14_regolith_reservoir/input.txt") as f:
        return f.read().strip()


class TestCave(unittest.TestCase):
    def test_sample(self):
        cave = Cave(sample_input)
        cave.draw()


if __name__ == "__main__":
    unittest.main()
