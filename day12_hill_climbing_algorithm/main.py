UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)


def add(a, b):
    (y1, x1), (y2, x2) = a, b
    return y1 + y2, x1 + x2


class World:
    def __init__(self, input):
        self.lines = input.splitlines()
        self.width = len(self.lines[0])
        self.height = len(self.lines)
        self.start = self.find_start()
        self.end = self.find_end()
        self.nodes = self.create_nodes()
        self.edges = self.create_edges()
        self.max_dist = 0

    def find_start(self):
        return self.find("S")

    def find_end(self):
        return self.find("E")

    def find(self, char):
        for y in range(self.height):
            for x in range(self.width):
                if self.lines[y][x] == char:
                    return (y, x)
        raise Exception(f"{char} not found!")

    def _print_state(self, distances):
        repr = ""
        max_dist = max([value for value in distances.values() if value != float("inf")])
        for y in range(self.height):
            for x in range(self.width):
                dist = distances.get((y, x), float("inf"))
                if dist == float("inf"):
                    dist = self.lines[y][x]
                    repr += f"{dist}"
                else:
                    repr += f"*"
            repr += "\n"
        repr += f"\nCurrent Max Dist: {max_dist}\n"
        print(repr)

    def create_nodes(self):
        nodes = set()
        for y in range(self.height):
            for x in range(self.width):
                nodes.add((y, x))
        return nodes

    def create_edges(self):
        edges = set()
        for node in self.nodes:
            new_edges = self.get_edges(node)
            for edge in new_edges:
                edges.add(edge)
        return edges

    def get_edges(self, node):
        candidates = [add(node, direction) for direction in [UP, DOWN, LEFT, RIGHT]]
        edges = [
            (node, candidate)
            for candidate in candidates
            if candidate in self.nodes and self.difference(node, candidate) < 2
        ]

        return edges

    def get_neighbours(self, node):
        return set([edge[1] for edge in self.edges if edge[0] == node])

    def difference(self, a, b):
        (y1, x1), (y2, x2) = a, b
        height1, height2 = self.lines[y1][x1], self.lines[y2][x2]
        if height1 == "S":
            height1 = "a"
        if height2 == "S":
            height2 = "a"
        if height1 == "E":
            height1 = "z"
        if height2 == "E":
            height2 = "z"
        return ord(height2) - ord(height1)

    def get_all_a(self):
        return [node for node in self.nodes if self.lines[node[0]][node[1]] == "a"]

    def shortest_path_from_any_a(self):
        starts = self.get_all_a()
        shortest_path = self.dijkstra(starts, self.end)
        return shortest_path

    def shortest_path_from_start(self):
        shortest_path = self.dijkstra([self.start], self.end)
        return shortest_path

    def dijkstra(self, starts, end):
        distances = {node: float("inf") for node in self.nodes}
        for start in starts:
            distances[start] = 0
        previous = {node: None for node in self.nodes}
        queue = self.nodes.copy()
        while queue:
            current = min(queue, key=lambda node: distances[node])
            queue.remove(current)
            if current == end:
                break
            for neighbour in self.get_neighbours(current):
                alt = distances[current] + 1
                if alt > self.max_dist:
                    self.max_dist = alt
                    self._print_state(distances)
                if alt < distances[neighbour]:
                    distances[neighbour] = alt
                    previous[neighbour] = current
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        return path
