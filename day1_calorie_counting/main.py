from itertools import groupby


def read_calories_from_file():
    with open("./day1_calorie_counting/input.txt", "r") as f:
        lines = f.readlines()
        groups = [list(g) for _, g in groupby(lines, lambda x: x == "\n")]
        groups = [group for group in groups if group != ["\n"]]
        return [[int(meal) for meal in meals] for meals in groups]


def main():
    calories_by_elf = read_calories_from_file()
    total_calories = [sum(meals) for meals in calories_by_elf]
    max_calories = max(total_calories)
    top_3_calories = sorted(total_calories, reverse=True)[:3]
    sum_top_3_calories = sum(top_3_calories)
    print(f"Max: ", max_calories)
    print(f"Top 3: ", top_3_calories)
    print(f"Sum Top 3: ", sum_top_3_calories)


if __name__ == "__main__":
    main()
