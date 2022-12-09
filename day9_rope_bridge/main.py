from enum import Enum


class Direction(Enum):
    LEFT = "L"
    RIGHT = "R"
    UP = "U"
    DOWN = "D"

    def to_vector(self):
        if self == Direction.LEFT:
            return (-1, 0)
        elif self == Direction.RIGHT:
            return (1, 0)
        elif self == Direction.UP:
            return (0, 1)
        elif self == Direction.DOWN:
            return (0, -1)


def move(object, direction):
    return tuple(map(sum, zip(object, direction)))


class Bridge:
    def __init__(self):
        self.head = (0, 0)
        self.tail = (0, 0)
        self.visited = set()

    def _move_tail(self):
        bridge = self
        diff = self.head[0] - self.tail[0], self.head[1] - self.tail[1]
        if abs(diff[0]) > 1 or abs(diff[1]) > 1:
            direction = diff[0], diff[1]
            if abs(direction[0]) > 1:
                direction = direction[0] // 2, direction[1]
            if abs(direction[1]) > 1:
                direction = direction[0], direction[1] // 2
            assert direction[0] in (-1, 0, 1) and direction[1] in (-1, 0, 1)
            self.tail = move(self.tail, direction)

    def step(self, direction):
        bridge = self
        self.head = move(self.head, direction.to_vector())
        self._move_tail()
        self.visited.add(self.tail)

    def multiple_steps(self, direction, count):
        bridge = self
        for _ in range(count):
            self.step(direction)

    visit_count = property(lambda self: len(self.visited))
