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


def update_segment(head, tail):
    diff = head[0] - tail[0], head[1] - tail[1]
    if abs(diff[0]) > 1 or abs(diff[1]) > 1:
        direction = diff[0], diff[1]
        if abs(direction[0]) > 1:
            direction = direction[0] // 2, direction[1]
        if abs(direction[1]) > 1:
            direction = direction[0], direction[1] // 2
        assert direction[0] in (-1, 0, 1) and direction[1] in (-1, 0, 1)
        tail = move(tail, direction)
    return head, tail


class Bridge:
    def __init__(self, length=2):
        self.rope = [(0, 0) for _ in range(length)]
        self.visited = set()

    def _update_rope(self):
        for i in range(len(self.rope) - 1):
            segment = update_segment(self.rope[i], self.rope[i + 1])
            self.rope[i] = segment[0]
            self.rope[i + 1] = segment[1]

    def step(self, direction):
        self.rope[0] = move(self.head, direction.to_vector())
        self._update_rope()
        self.visited.add(self.tail)

    def multiple_steps(self, direction, count):
        for _ in range(count):
            self.step(direction)

    visit_count = property(lambda self: len(self.visited))
    head = property(lambda self: self.rope[0])
    tail = property(lambda self: self.rope[-1])
