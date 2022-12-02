from enum import Enum


class Choice(Enum):
    A = "A"
    B = "B"
    C = "C"
    X = "X"
    Y = "Y"
    Z = "Z"

    def toShape(self):
        if self in rock:
            return Shape.ROCK
        elif self in paper:
            return Shape.PAPER
        elif self in scisor:
            return Shape.SCISSORS

    def toOutcome(self):
        return Outcome(self.value)


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(Enum):
    LOOSE = "X"
    DRAW = "Y"
    WIN = "Z"


LOST = 0
DRAW = 3
WIN = 6

rock = Choice.A, Choice.X
paper = Choice.B, Choice.Y
scisor = Choice.C, Choice.Z

# Determine the score for a game
def win_score(a: Shape, b: Shape):
    match a:
        case Shape.ROCK:
            match b:
                case Shape.ROCK:
                    return DRAW
                case Shape.PAPER:
                    return LOST
                case Shape.SCISSORS:
                    return WIN
        case Shape.PAPER:
            match b:
                case Shape.ROCK:
                    return WIN
                case Shape.PAPER:
                    return DRAW
                case Shape.SCISSORS:
                    return LOST
        case Shape.SCISSORS:
            match b:
                case Shape.ROCK:
                    return LOST
                case Shape.PAPER:
                    return WIN
                case Shape.SCISSORS:
                    return DRAW


# Make stragegic choice based on the desired outcome
def strategy_choice(opponent: Shape, outcome: Outcome) -> Shape:
    match outcome:
        case Outcome.DRAW:
            return opponent
        case Outcome.LOOSE:
            match opponent:
                case Shape.ROCK:
                    return Shape.SCISSORS
                case Shape.PAPER:
                    return Shape.ROCK
                case Shape.SCISSORS:
                    return Shape.PAPER
        case Outcome.WIN:
            match opponent:
                case Shape.ROCK:
                    return Shape.PAPER
                case Shape.PAPER:
                    return Shape.SCISSORS
                case Shape.SCISSORS:
                    return Shape.ROCK


class Game:
    def __init__(self, opponent: Choice, target: Choice):
        self.opponent = opponent.toShape()
        self.target = target.toOutcome()
        self.choice = strategy_choice(self.opponent, self.target)

    def score(self):
        score = self.choice.value
        return score + win_score(self.choice, self.opponent)

    def __repr__(self) -> str:
        return f"{self.opponent.name} vs {self.choice.name}: {self.score()}"


def read_games_from_file():
    with open("./day2_rock_paper_scissors/input.txt", "r") as f:
        lines = f.readlines()
        # lines = ["A Y", "B X", "C Z"]
        return [
            [Choice(choice.strip()) for choice in line.split(" ")] for line in lines
        ]


def main():
    shapes = read_games_from_file()
    games = [Game(*shape) for shape in shapes]
    scores = [game.score() for game in games]
    print(games)
    print(sum(scores))


if __name__ == "__main__":
    main()
