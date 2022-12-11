new_line = "\n"
important_steps = [20, 60, 100, 140, 180, 220]


class Instruction:
    def __init__(self, line):
        self.line = line
        self.opcode = line.split()[0]
        self.steps = 1
        if self.opcode == "noop":
            self.operand = 0
        else:
            self.operand = int(line.split()[1])
            self.steps = 2


class CathodeRayTube:
    def __init__(self, instructions):
        self.cycle = 1
        self.line = 0
        self.X = 1
        self.output = ""
        self.instructions = [Instruction(line) for line in instructions.splitlines()]

    def step(self, cycles=1):
        for _ in range(cycles):
            self._step()

    def _step(self):
        self._update_output()
        operation = self.instruction
        operation.steps -= 1
        if operation.steps == 0:
            self.line += 1
            self.X += operation.operand
        self.cycle += 1

    def _signal_strength(self):
        return self.cycle * self.X

    def _instruction(self):
        return self.instructions[self.line]

    def _sprite(self):
        pos = self.X
        return [pos - 1, pos, pos + 1]

    def sum_of_signal_strengths(self):
        strengths = []
        steps = important_steps[-1]
        for _ in range(steps):
            self._step()
            if self.cycle in important_steps:
                strengths.append(self.signal_strength)
        return sum(strengths)

    def _update_output(self):
        pos = self.cycle - 1
        if pos % 40 in self.sprite:
            self.output += "#"
        else:
            self.output += "."
        if self.cycle % 40 == 0:
            self.output += new_line

    instruction = property(_instruction)
    signal_strength = property(_signal_strength)
    sprite = property(_sprite)
