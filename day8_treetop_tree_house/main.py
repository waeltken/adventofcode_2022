from math import prod

new_line = "\n"

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def read_input():
    with open("./day8_treetop_tree_house/input.txt") as f:
        return f.readlines()


def create_tree_map(input):
    return [[int(char) for char in line.strip()] for line in input]


class Wood:
    def __init__(self, input) -> None:
        self.map = create_tree_map(input)

    def is_tree_visible_from(self, tree, direction):
        row, col = tree
        height = self.map[row][col]
        while True:
            row += direction[0]
            col += direction[1]
            if row < 0 or col < 0:
                # We've gone off the edge of the map
                return True
            try:
                if self.map[row][col] >= height:
                    # There is another tree in the way
                    return False
            except IndexError:
                # We've gone off the edge of the map
                return True

    def is_visible(self, tree):
        return any(
            [self.is_tree_visible_from(tree, direction) for direction in directions]
        )

    def subscore(self, tree, direction):
        row, col = tree
        height = self.map[row][col]
        score = 0
        while True:
            row += direction[0]
            col += direction[1]
            if row < 0 or col < 0:
                # We've gone off the edge of the map
                return score
            try:
                if self.map[row][col] >= height:
                    # There is another tree in the way
                    score += 1
                    return score
                score += 1
            except IndexError:
                # We've gone off the edge of the map
                return score

    def scenic_score(self, tree):
        return prod([self.subscore(tree, direction) for direction in directions])

    def max_scenic_score(self):
        return max([self.scenic_score(tree) for tree in self.trees])

    def visible_trees(self):
        visible = set()
        for tree in self.trees:
            if self.is_visible(tree):
                visible.update((tree,))
        return visible

    def _trees(self):
        return [(x, y) for x in range(len(self.map)) for y in range(len(self.map[0]))]

    trees = property(_trees)

    def __repr__(self):
        return new_line.join([str(row) for row in self.map])
