import unittest

from main import CathodeRayTube

small_sample_input = """noop
addx 3
addx -5"""

sample_input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

sample_output = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""


def read_input():
    with open("./day10_cathode_ray_tube/input.txt") as f:
        return f.read()


class TestCathodeRayTube(unittest.TestCase):
    def testSmallSampleInput(self):
        cathode_ray_tube = CathodeRayTube(small_sample_input)
        cathode_ray_tube.step()
        self.assertEqual(cathode_ray_tube.cycle, 2)
        self.assertEqual(cathode_ray_tube.X, 1)
        self.assertEqual(cathode_ray_tube.signal_strength, 2)
        cathode_ray_tube.step()
        self.assertEqual(cathode_ray_tube.X, 1)
        cathode_ray_tube.step()
        self.assertEqual(cathode_ray_tube.X, 4)
        cathode_ray_tube.step()
        self.assertEqual(cathode_ray_tube.X, 4)
        cathode_ray_tube.step()
        self.assertEqual(cathode_ray_tube.X, -1)
        self.assertEqual(cathode_ray_tube.signal_strength, -6)

    def testSampleInput(self):
        cathode_ray_tube = CathodeRayTube(sample_input)
        cathode_ray_tube.step(19)
        self.assertEqual(cathode_ray_tube.signal_strength, 420)
        cathode_ray_tube.step(40)
        self.assertEqual(cathode_ray_tube.signal_strength, 1140)
        cathode_ray_tube.step(40)
        self.assertEqual(cathode_ray_tube.signal_strength, 1800)
        cathode_ray_tube.step(40)
        self.assertEqual(cathode_ray_tube.signal_strength, 2940)
        cathode_ray_tube.step(40)
        self.assertEqual(cathode_ray_tube.signal_strength, 2880)
        cathode_ray_tube.step(40)
        self.assertEqual(cathode_ray_tube.cycle, 220)
        self.assertEqual(cathode_ray_tube.X, 18)
        self.assertEqual(cathode_ray_tube.signal_strength, 3960)
        cathode_ray_tube = CathodeRayTube(sample_input)
        self.assertEqual(cathode_ray_tube.sum_of_signal_strengths(), 13140)

    def testInput(self):
        cathode_ray_tube = CathodeRayTube(read_input())
        self.assertEqual(cathode_ray_tube.sum_of_signal_strengths(), 14360)
        cathode_ray_tube.step(20)
        print("\n")
        print("\n")
        print(cathode_ray_tube.output)

    def testSampleOutput(self):
        cathode_ray_tube = CathodeRayTube(sample_input)
        cathode_ray_tube.step()
        self.assertEqual(cathode_ray_tube.output, "#")
        cathode_ray_tube.step()
        self.assertEqual(cathode_ray_tube.output, "##")
        cathode_ray_tube.step()
        self.assertEqual(cathode_ray_tube.output, "##.")
        cathode_ray_tube.step()
        self.assertEqual(cathode_ray_tube.output, "##..")
        cathode_ray_tube.step(4)
        self.assertEqual(cathode_ray_tube.output, "##..##..")
        cathode_ray_tube.step()
        self.assertEqual(cathode_ray_tube.cycle, 10)
        self.assertEqual(cathode_ray_tube.output, "##..##..#")
        cathode_ray_tube.step()
        self.assertEqual(cathode_ray_tube.cycle, 11)
        self.assertEqual(cathode_ray_tube.output, "##..##..##")
        cathode_ray_tube.step(11)
        self.assertEqual(cathode_ray_tube.cycle, 22)
        self.assertEqual(len(cathode_ray_tube.output), 21)
        self.assertEqual(cathode_ray_tube.output, "##..##..##..##..##..#")
        cathode_ray_tube.step(19)
        self.assertEqual(cathode_ray_tube.cycle, 41)
        self.assertEqual(
            cathode_ray_tube.output, "##..##..##..##..##..##..##..##..##..##..\n"
        )
        cathode_ray_tube.step(200)
        self.assertEqual(cathode_ray_tube.cycle, 241)
        self.assertEqual(cathode_ray_tube.output, sample_output)


if __name__ == "__main__":
    unittest.main()
