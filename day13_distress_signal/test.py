import unittest

from main import IntcodeComputer

sample_input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def read_input():
    with open("day13_distress_signal/input.txt") as f:
        return f.read().strip()


class TestDay13(unittest.TestCase):
    def test_sample(self):
        computer = IntcodeComputer(sample_input)
        pairs_in_order = computer.pairs_in_order()
        self.assertEqual(len(computer.pairs), 8)
        self.assertEqual(
            pairs_in_order,
            [True, True, False, True, False, True, False, False],
        )
        self.assertEqual(computer.sum_true_indices(), 13)

    def test_input(self):
        computer = IntcodeComputer(read_input())
        self.assertEqual(len(computer.pairs), 150)
        self.assertEqual(computer.sum_true_indices(), 4010)


if __name__ == "__main__":
    unittest.main()
