from math import prod
from functools import cmp_to_key

dividers = [[2]], [[6]]


class IntcodeComputer:
    def __init__(self, input):
        self.input = input
        self.pairs = [pair.split("\n") for pair in input.split("\n\n")]
        self.pairs = [[eval(left), eval(right)] for left, right in self.pairs]
        self.lines = [line for line in self.input.split("\n") if line.strip() != ""]
        self.lists = [eval(line) for line in self.lines]
        self.lists += dividers
        self.lists = sorted(self.lists, key=cmp_to_key(compare))

    def pairs_in_order(self):
        return [compare(left, right) < 0 for (left, right) in self.pairs]

    def sum_true_indices(self):
        return sum_true_indices(self.pairs_in_order())

    def prod_divider_indices(self):
        divider_indices = [
            index + 1 for index, value in enumerate(self.lists) if value in dividers
        ]
        return prod(divider_indices)


def compare(left_list, right_list):
    if not left_list and right_list:
        return -1
    if not right_list and left_list:
        return 1
    if not left_list and not right_list:
        return 0
    left, *left_tail = left_list
    right, *right_tail = right_list
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        return compare(left_tail, right_tail)
    # check if left and right are lists
    if isinstance(left, list) and isinstance(right, list):
        if compare(left, right) == 0:
            return compare(left_tail, right_tail)
        return compare(left, right)
    # check if left is a list and right is an int
    if isinstance(left, list) and isinstance(right, int):
        return compare([left, *left_tail], [[right], *right_tail])
    if isinstance(left, int) and isinstance(right, list):
        return compare([[left], *left_tail], [right, *right_tail])


def sum_true_indices(pairs_in_order):
    return sum([index + 1 for index, value in enumerate(pairs_in_order) if value])
