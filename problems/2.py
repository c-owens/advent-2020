
from .problem import Problem

class Day2(Problem):
    """
    Solution for https://adventofcode.com/2020/day/2
    """

    def __init__(self):
        Problem.__init__(self)

        # Convert the input lines to tuples of direction + unit
        self.input_vals = []
        for item in self.input:
            parts = item.split()
            self.input_vals.append((parts[0], int(parts[1])))

    def solve_a(self) -> int:
        horizontal_pos = 0
        depth = 0
        for item in self.input_vals:
            val = item[1]
            match item[0]:
                case "forward":
                    horizontal_pos += val
                case "down":
                    depth += val
                case "up":
                    depth -= val
        print(f"Horizontal position = {horizontal_pos}, depth = {depth}")
        answer = horizontal_pos * depth
        print(f"Horizontal x Depth = {answer}")
        return answer

    def solve_b(self) -> int:
        horizontal_pos = 0
        depth = 0
        aim = 0
        for item in self.input_vals:
            val = item[1]
            match item[0]:
                case "forward":
                    horizontal_pos += val
                    depth_inc = aim * val
                    depth += depth_inc
                case "down":
                    aim += val
                case "up":
                    aim -= val
        print(f"Horizontal position = {horizontal_pos}, depth = {depth}, aim = {aim}")
        answer = horizontal_pos * depth
        print(f"Horizontal x Depth = {answer}")
        return answer

    @property
    def name(self) -> str:
        return "Day 2: Dive"

    @property
    def number(self) -> int:
        return 2
