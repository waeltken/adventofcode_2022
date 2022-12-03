from typing import Tuple
from numpy import reshape

sample_strings = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]

Backpack = Tuple[str, str]


def split_backpack(backpack: str) -> Backpack:
    return backpack[: len(backpack) // 2], backpack[len(backpack) // 2 :]


def find_duplicate(backpack: Backpack) -> chr:
    (left, right) = backpack
    for letter in left:
        if letter in right:
            return letter


def item_priority(chr) -> int:
    return ord(chr) - 96 if chr.islower() else ord(chr) - 38


assert item_priority("a") == 1
assert item_priority("z") == 26
assert item_priority("L") == 38
assert item_priority("P") == 42


def read_lines_from_file():
    with open("./day3_backpacks/input.txt", "r") as f:
        return f.readlines()


def group_elves_backpacks(backpacks: list) -> list:
    return reshape(backpacks, (-1, 3))


def find_label_item(backpacks: list) -> chr:
    all_items = "".join(backpacks)
    for item in all_items:
        (a, b, c) = backpacks
        if item in a and item in b and item in c:
            return item


def main():
    backpacks = [split_backpack(backpack) for backpack in sample_strings]
    backpacks = [split_backpack(backpack) for backpack in read_lines_from_file()]
    for backpack in backpacks:
        duplicate = find_duplicate(backpack)
        print(
            f"Backpack: {backpack}, Duplicate letter: ({duplicate}, {item_priority(duplicate)})",
        )
    item_priorities = [
        item_priority(find_duplicate(backpack)) for backpack in backpacks
    ]
    print(f"Sum of item priorities: {sum(item_priorities)}")

    groups = group_elves_backpacks(sample_strings)
    groups = group_elves_backpacks(read_lines_from_file())

    label_items = [find_label_item(group) for group in groups]
    label_item_priorities = [item_priority(item) for item in label_items]
    print(f"Sum of label item priorities: {sum(label_item_priorities)}")


if __name__ == "__main__":
    main()
