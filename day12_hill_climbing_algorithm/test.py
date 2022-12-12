import unittest

from main import World

simple_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


def read_input():
    with open("day12_hill_climbing_algorithm/input.txt") as f:
        return f.read()


class TestShortestPath(unittest.TestCase):
    def test_simple(self):
        world = World(simple_input)
        self.assertEqual(world.start, (0, 0))
        self.assertEqual(world.end, (2, 5))
        self.assertEqual(world.difference(world.start, (0, 1)), 0)
        self.assertEqual(len(world.nodes), 40)
        self.assertEqual(len(world.edges), 111)
        self.assertIn(((0, 0), (0, 1)), world.edges)
        self.assertIn(((0, 0), (1, 0)), world.edges)
        self.assertEqual(world.get_neighbours((0, 0)), {(0, 1), (1, 0)})
        path = world.shortest_path_from_start()
        print(path)
        self.assertEqual(len(path) - 1, 31)

    def test_input_from_start(self):
        world = World(read_input())
        path = world.shortest_path_from_start()
        print(path)
        self.assertEqual(len(path) - 1, 534)

    def test_input_from_any_a(self):
        world = World(read_input())
        path = world.shortest_path_from_any_a()
        print(path)
        self.assertEqual(len(path) - 1, 525)


if __name__ == "__main__":
    unittest.main()
