from .problem import Problem
import math

class Day3(Problem):
    """
    Solution for https://adventofcode.com/2020/day/3
    """

    def __init__(self):
        Problem.__init__(self)

    def solve(self, x_distance : int, y_distance : int) -> int:
        height = len(self.input)
        width = len(self.input[0])

        # Starting with 0, 0 at the top left, the first index is the row offset and the 
        # second index is the column offset.
        row = 0
        col = 0
        collisions = 0
        while row <= height - 1:
            # Convert the total column number we want to check into the corresponding
            # column value in the smaller input data.
            x = col
            if x >= width:
                 x = x % width

            if self.input[row][x] == "#":
                collisions += 1
            col += x_distance
            row += y_distance

        return collisions

    def solve_a(self) -> int:
        collisions = self.solve(x_distance=3, y_distance=1)
        print(f"{collisions} collisions detected")

    def solve_b(self) -> int:
        # The same as the a solution, but do it with 5 different distances and multiply them
        a = self.solve(x_distance=1, y_distance=1)
        b = self.solve(x_distance=3, y_distance=1)
        c = self.solve(x_distance=5, y_distance=1)
        d = self.solve(x_distance=7, y_distance=1)
        e = self.solve(x_distance=1, y_distance=2)
        solution = a * b * c * d * e
        print(f"{solution} collisions multiplied")

    @property
    def name(self) -> str:
        return "Day 3: Toboggan Trajectory"

    @property
    def number(self) -> int:
        return 3
