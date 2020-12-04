from .problem import Problem
import math

class Day3(Problem):
    """
    Solution for https://adventofcode.com/2020/day/3
    """

    def __init__(self):
        Problem.__init__(self)

    def solve_a(self) -> int:
        # The input needs to be tiled to the right N number of times, determine how many times
        # to tile it by calculating how many times we need to move right 3 spaces given the height.
        # This is not exact due to the use of floor and ceil but will guarantee we have enough tiles
        # to get to the end.
        height = len(self.input)
        width = len(self.input[0])
        num_moves = height * 3
        num_moves_per_tile = math.floor(width / 3)
        tiles_count = math.ceil(num_moves / num_moves_per_tile)

        # Generate the tiles as a list of strings.
        tiled_input = []
        for line in self.input:
            # In python you can multiply a collection to repeat it
            val = line * tiles_count
            tiled_input.append(val)

        # Starting with 0, 0 at the top left, the first index is the row offset and the 
        # second index is the column offset.
        row = 0
        col = 0
        collisions = 0
        while row <= len(tiled_input) - 1:
            row_val = tiled_input[row]
            char = row_val[col]
            if char == "#":
                collisions += 1
            col = col + 3
            row = row + 1

        print(f"Number of trees hit = {collisions}")

    def solve_b(self) -> int:
        pass

    @property
    def name(self) -> str:
        return "Day 3: Toboggan Trajectory"

    @property
    def number(self) -> int:
        return 3
