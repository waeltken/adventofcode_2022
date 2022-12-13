class IntcodeComputer:
    def __init__(self, input):
        self.input = input
        self.pairs = [pair.split("\n") for pair in input.split("\n\n")]
        self.pairs = [[eval(left), eval(right)] for left, right in self.pairs]

    def pairs_in_order(self):
        return [is_in_order(pair) for pair in self.pairs]

    def sum_true_indices(self):
        return sum_true_indices(self.pairs_in_order())


def is_in_order(pair):
    left_list, right_list = pair
    if not left_list:
        return True
    if not right_list:
        return False
    left, *left_tail = left_list
    right, *right_tail = right_list
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return False
        return is_in_order([left_tail, right_tail])
    # check if left and right are lists
    if isinstance(left, list) and isinstance(right, list):
        return is_in_order([left, right])
    # check if left is a list and right is an int
    if isinstance(left, list) and isinstance(right, int):
        return is_in_order([[left, *left_tail], [[right], *right_tail]])
    if isinstance(left, int) and isinstance(right, list):
        return is_in_order([[[left], *left_tail], [right, *right_tail]])


def sum_true_indices(pairs_in_order):
    return sum([index + 1 for index, value in enumerate(pairs_in_order) if value])
