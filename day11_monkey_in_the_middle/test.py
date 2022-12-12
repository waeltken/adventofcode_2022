import unittest

from main import MonkeyGame

test_monkey_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


def read_input():
    with open("day11_monkey_in_the_middle/input.txt") as f:
        return f.read()


class TestMonkeys(unittest.TestCase):
    def test_monkeys(self):
        game = MonkeyGame(test_monkey_input)
        self.assertEqual(len(game.monkeys), 4)
        monkey0, monkey1, monkey2, monkey3 = game.monkeys
        self.assertEqual(monkey0.items, [79, 98])
        self.assertEqual(monkey0.operation(5), 95)
        self.assertTrue(monkey0._test(23))
        self.assertFalse(monkey0._test(24))
        self.assertEqual(monkey1.items, [54, 65, 75, 74])
        self.assertEqual(monkey1.operation(5), 11)
        self.assertTrue(monkey1._test(19))
        self.assertEqual(monkey2.items, [79, 60, 97])
        self.assertEqual(monkey2.operation(5), 25)
        self.assertTrue(monkey2._test(13))
        self.assertEqual(monkey3.items, [74])
        self.assertEqual(monkey3.operation(5), 8)
        self.assertTrue(monkey3._test(17))
        game.play_round()
        self.assertEqual(monkey0.items, [20, 23, 27, 26])
        self.assertEqual(monkey1.items, [2080, 25, 167, 207, 401, 1046])
        self.assertEqual(monkey2.items, [])
        self.assertEqual(monkey3.items, [])
        game.play_round()
        self.assertEqual(monkey0.items, [695, 10, 71, 135, 350])
        self.assertEqual(monkey1.items, [43, 49, 58, 55, 362])
        self.assertEqual(monkey2.items, [])
        self.assertEqual(monkey3.items, [])
        game.play_round()
        self.assertEqual(monkey0.items, [16, 18, 21, 20, 122])
        self.assertEqual(monkey1.items, [1468, 22, 150, 286, 739])
        self.assertEqual(monkey2.items, [])
        self.assertEqual(monkey3.items, [])
        game.play_round()
        self.assertEqual(monkey0.items, [491, 9, 52, 97, 248, 34])
        self.assertEqual(monkey1.items, [39, 45, 43, 258])
        self.assertEqual(monkey2.items, [])
        self.assertEqual(monkey3.items, [])
        game.play_round()
        self.assertEqual(monkey0.items, [15, 17, 16, 88, 1037])
        self.assertEqual(monkey1.items, [20, 110, 205, 524, 72])
        self.assertEqual(monkey2.items, [])
        self.assertEqual(monkey3.items, [])
        game.play_round()
        self.assertEqual(monkey0.items, [8, 70, 176, 26, 34])
        self.assertEqual(monkey1.items, [481, 32, 36, 186, 2190])
        self.assertEqual(monkey2.items, [])
        self.assertEqual(monkey3.items, [])
        game.play_round()
        self.assertEqual(monkey0.items, [162, 12, 14, 64, 732, 17])
        self.assertEqual(monkey1.items, [148, 372, 55, 72])
        self.assertEqual(monkey2.items, [])
        self.assertEqual(monkey3.items, [])
        game.play_round()
        self.assertEqual(monkey0.items, [51, 126, 20, 26, 136])
        self.assertEqual(monkey1.items, [343, 26, 30, 1546, 36])
        self.assertEqual(monkey2.items, [])
        self.assertEqual(monkey3.items, [])
        game.play_round()
        self.assertEqual(monkey0.items, [116, 10, 12, 517, 14])
        self.assertEqual(monkey1.items, [108, 267, 43, 55, 288])
        self.assertEqual(monkey2.items, [])
        self.assertEqual(monkey3.items, [])
        game.play_round()
        self.assertEqual(monkey0.items, [91, 16, 20, 98])
        self.assertEqual(monkey1.items, [481, 245, 22, 26, 1092, 30])
        self.assertEqual(monkey2.items, [])
        self.assertEqual(monkey3.items, [])
        game.play_round()
        game.play_round()
        game.play_round()
        game.play_round()
        game.play_round()
        self.assertEqual(monkey0.items, [83, 44, 8, 184, 9, 20, 26, 102])
        self.assertEqual(monkey1.items, [110, 36])
        self.assertEqual(monkey2.items, [])
        self.assertEqual(monkey3.items, [])
        game.play_round()
        game.play_round()
        game.play_round()
        game.play_round()
        game.play_round()
        self.assertEqual(monkey0.items, [10, 12, 14, 26, 34])
        self.assertEqual(monkey1.items, [245, 93, 53, 199, 115])
        self.assertEqual(monkey2.items, [])
        self.assertEqual(monkey3.items, [])
        self.assertEqual(game.prod_max2_inspected(), 10605)

    def test_monkeys_worried(self):
        game = MonkeyGame(test_monkey_input, worried=True)
        monkey0, monkey1, monkey2, monkey3 = game.monkeys
        game.play_round()
        self.assertEqual(monkey0.inspected_count, 2)
        self.assertEqual(monkey1.inspected_count, 4)
        self.assertEqual(monkey2.inspected_count, 3)
        self.assertEqual(monkey3.inspected_count, 6)
        for _ in range(19):
            game.play_round()
        self.assertEqual(monkey0.inspected_count, 99)
        self.assertEqual(monkey1.inspected_count, 97)
        self.assertEqual(monkey2.inspected_count, 8)
        self.assertEqual(monkey3.inspected_count, 103)
        for _ in range(980):
            game.play_round()
        self.assertEqual(monkey0.inspected_count, 5204)
        self.assertEqual(monkey1.inspected_count, 4792)
        self.assertEqual(monkey2.inspected_count, 199)
        self.assertEqual(monkey3.inspected_count, 5192)

    def test_input(self):
        game = MonkeyGame(read_input())
        for _ in range(20):
            game.play_round()
        self.assertEqual(game.prod_max2_inspected(), 69918)

    def test_worried_input(self):
        game = MonkeyGame(read_input(), worried=True)
        for _ in range(10000):
            game.play_round()
        self.assertEqual(game.prod_max2_inspected(), 19573408701)


if __name__ == "__main__":
    unittest.main()
