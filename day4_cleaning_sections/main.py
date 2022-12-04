filename = "day4_cleaning_sections/input.txt"
sample_input = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]


def unwrap_pair(pair):
    (left, right) = pair.split(",")
    return (create_range(left), create_range(right))


def create_range(input):
    (left, right) = input.split("-")
    return range(int(left), int(right) + 1)


def ranges_overlap_completley(range1, range2):
    return all(e in range2 for e in range1) or all(e in range1 for e in range2)


def ranges_overlap(range1, range2):
    return any(e in range2 for e in range1)


def main():
    ranges = [unwrap_pair(pair) for pair in sample_input]
    ranges = [unwrap_pair(pair) for pair in open(filename).read().splitlines()]
    complete_overlaps = [
        ranges_overlap_completley(left, right) for (left, right) in ranges
    ]
    overlaps = [ranges_overlap(left, right) for (left, right) in ranges]
    print(ranges)
    print(complete_overlaps)
    print(f"Complete Overlaps: {sum(complete_overlaps)})")
    print(f"Partial Overlaps: {sum(overlaps)})")


if __name__ == "__main__":
    main()
