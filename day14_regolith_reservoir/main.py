class Cave:
    def __init__(self, input):
        input_lines = input.splitlines()
        lines_strings = [line.split(" -> ") for line in input_lines]
        self.lines = [
            [tuple(map(int, string.split(","))) for string in line_strings]
            for line_strings in lines_strings
        ]
        self.lines.append([(500, 0)])
        all_points = [point for line in self.lines for point in line]
        self.max_x = max(all_points, key=lambda point: point[0])[0]
        self.max_y = max(all_points, key=lambda point: point[1])[1]
        self.min_x = min(all_points, key=lambda point: point[0])[0]
        self.min_y = min(all_points, key=lambda point: point[1])[1]

    def get_row(self, y):
        return ["#", "."] * (self.max_y - self.min_y + 1)

    def draw(self) -> None:
        format_row = "{:>1}" * (self.max_y - self.min_y + 1)
        for y in range(self.min_x, self.max_x + 1):
            print(format_row.format("", *self.get_row(y)))
