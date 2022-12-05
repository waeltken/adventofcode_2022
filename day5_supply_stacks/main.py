import re
import numpy as np

MOVES_FILE = "day5_supply_stacks/moves.txt"
STATE_FILE = "day5_supply_stacks/state.txt"


def main():
    moves = read_moves()
    state = read_state()
    state.apply_moves(moves)
    print(state.peek())


def read_lines_from(file_name):
    with open(file_name, "r") as f:
        return f.readlines()


class Move:
    def __init__(self, count: int, start: int, stop: int):
        self.count = count
        self.start = start
        self.stop = stop

    def __repr__(self) -> str:
        return f"move {self.count} from {self.start} to {self.stop}"


class State:
    def __init__(self, stacks: list):
        self.stacks = stacks

    def apply(self, move: Move):
        crane = []
        for _ in range(move.count):
            crane.append(self.stacks[move.start].pop())
        crane.reverse()
        for item in crane:
            self.stacks[move.stop].append(item)

    def apply_moves(self, moves: list):
        for move in moves:
            self.apply(move)

    def peek(self):
        return "".join([stack[-1] for stack in self.stacks])


def read_moves():
    lines = read_lines_from(MOVES_FILE)
    input = [re.findall(r"\d+", line) for line in lines]
    return [
        Move(int(count), int(start) - 1, int(stop) - 1) for count, start, stop in input
    ]


def read_state():
    lines = read_lines_from(STATE_FILE)
    input = [re.findall(r"\[(\S+)\]|\s\s\s\s?", line) for line in lines]
    input = np.flip(np.transpose(input), 1).tolist()
    for i in range(len(input)):
        input[i] = [j for j in input[i] if j != ""]
    return State(input)


if __name__ == "__main__":
    main()
