class IntcodeComputer:
    def __init__(self, input):
        self.input = input
        self.pairs = [pair.split("\n") for pair in input.split("\n\n")]
