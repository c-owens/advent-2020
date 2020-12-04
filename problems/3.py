from .problem import Problem
import math

class Day3(Problem):
    """
    Solution for https://adventofcode.com/2020/day/3
    """

    def __init__(self):
        Problem.__init__(self)

    def solve(self, x: int, y: int) -> int:
        height = len(self.input)
        width = len(self.input[0])

        # Starting with 0, 0 at the top left, the first index is the row offset and the 
        # second index is the column offset.
        col = 0
        collisions = 0
        for row in range(0, height, y):
            if self.input[row][col % width] == "#":
                collisions += 1
            col += x

        return collisions

    def solve_a(self) -> int:
        collisions = self.solve(x=3, y=1)
        print(f"{collisions} collisions detected")

    def solve_b(self) -> int:
        # The same as the A solution, but do it with 5 different slopes and multiply the results
        a = self.solve(x=1, y=1)
        b = self.solve(x=3, y=1)
        c = self.solve(x=5, y=1)
        d = self.solve(x=7, y=1)
        e = self.solve(x=1, y=2)
        solution = a * b * c * d * e
        print(f"{solution} collisions multiplied")

    @property
    def name(self) -> str:
        return "Day 3: Toboggan Trajectory"

    @property
    def number(self) -> int:
        return 3
