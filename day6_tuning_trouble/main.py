from collections.abc import Callable
import unittest


class TestSignalDetector(unittest.TestCase):
    def test_find_packet_marker(self):
        self.assertEqual(find_packet_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 7)
        self.assertEqual(find_packet_marker("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5)
        self.assertEqual(find_packet_marker("nppdvjthqldpwncqszvftbrmjlhg"), 6)
        self.assertEqual(find_packet_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 10)
        self.assertEqual(find_packet_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 11)


def find_marker(length: int) -> Callable[[str], int]:
    def marker(signal: str) -> int:
        buffer = []
        for i in range(len(signal)):
            char = signal[i]
            if char in buffer:
                last = buffer.index(char)
                buffer = buffer[last + 1 :]
            buffer.append(char)
            if len(buffer) == length:
                return i + 1

    return marker


def find_packet_marker(signal: str) -> int:
    return find_marker(4)(signal)


def find_message_marker(signal: str) -> int:
    return find_marker(14)(signal)


def main():
    with open("./day6_tuning_trouble/input.txt") as f:
        signal = f.read()
        print(find_packet_marker(signal))
        print(find_message_marker(signal))


if __name__ == "__main__":
    main()
    unittest.main()
