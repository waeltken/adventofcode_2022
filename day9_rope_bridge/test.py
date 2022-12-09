import unittest

from main import Bridge, Direction


class TestBridge(unittest.TestCase):
    def test_one_step(self):
        bridge = Bridge()
        bridge.step(Direction.UP)
        self.assertEqual(bridge.head, (0, 1))
        self.assertEqual(bridge.tail, (0, 0))
        self.assertEqual(bridge.visited, {(0, 0)})
        bridge.step(Direction.UP)
        self.assertEqual(bridge.head, (0, 2))
        self.assertEqual(bridge.tail, (0, 1))
        bridge.step(Direction.RIGHT)
        self.assertEqual(bridge.head, (1, 2))
        self.assertEqual(bridge.tail, (0, 1))
        bridge.step(Direction.RIGHT)
        self.assertEqual(bridge.head, (2, 2))
        self.assertEqual(bridge.tail, (1, 2))
        self.assertEqual(bridge.visited, {(0, 0), (0, 1), (1, 2)})

    def test_multi_step(self):
        bridge = Bridge()
        bridge.multiple_steps(Direction.UP, 3)
        self.assertEqual(bridge.head, (0, 3))
        self.assertEqual(bridge.tail, (0, 2))
        self.assertEqual(bridge.visited, {(0, 0), (0, 1), (0, 2)})
        self.assertEqual(bridge.visit_count, 3)

    def test_run_input(self):
        bridge = Bridge()
        for line in read_input():
            direction, count = Direction(line[0]), int(line[1:])
            bridge.multiple_steps(direction, count)
        self.assertEqual(bridge.visit_count, 6339)


def read_input():
    with open("./day9_rope_bridge/input.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    unittest.main()
