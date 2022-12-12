import re

from math import gcd
from functools import cached_property


class MonkeyGame:
    def __init__(self, input, worried=False):
        self.monkeys = parse_monkeys(input)
        for monkey in self.monkeys:
            monkey.game = self
            monkey.worried = worried

    def play_round(self):
        for monkey in self.monkeys:
            monkey.play()

    def prod_max2_inspected(self):
        inspect_counts = [monkey.inspected_count for monkey in self.monkeys]
        inspect_counts.sort(reverse=True)
        return inspect_counts[0] * inspect_counts[1]

    @cached_property
    def least_common_multiple(self):
        divisors = [monkey.divisor for monkey in self.monkeys]
        lcm = 1
        for i in divisors:
            lcm = lcm * i // gcd(lcm, i)
        return lcm


class Monkey:
    def __init__(self, starting_items, operation, divisor, throw_to, worried=False):
        self.items = starting_items
        self._operation = operation
        self.divisor = divisor
        self._test = lambda x: x % self.divisor == 0
        self._throw_to_targets = throw_to
        self.game = None
        self.inspected_count = 0
        self.worried = worried

    def operation(self, old):
        old = old  # old is important for eval
        return eval(self._operation)

    def play(self):
        current_items = self.items.copy()
        self.items = []
        for item in current_items:
            item = self.inspect(item)
            self.throw(item)

    def inspect(self, item):
        self.inspected_count += 1
        if self.worried:
            return self.operation(item) % self.game.least_common_multiple
        return self.operation(item) // 3

    def throw(self, item):
        if self._test(item):
            target = self._throw_to_targets[0]
        else:
            target = self._throw_to_targets[1]
        self.game.monkeys[target].items.append(item)


def parse_monkey(input):
    lines = input.strip().split("\n")
    starting_items = [int(item) for item in lines[1].split(": ")[1].split(", ")]
    operation = lines[2].split("= ")[1]
    divisor = int(re.findall(r"\d+", lines[3])[0])
    throw_to = [int(re.findall(r"\d+", line)[0]) for line in lines[4:]]
    return Monkey(starting_items, operation, divisor, throw_to)


def parse_monkeys(input):
    monkey_input = input.split("\n\n")
    monkeys = [parse_monkey(monkey) for monkey in monkey_input]
    return monkeys
