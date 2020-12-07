
from .problem import Problem
import math

class Day5(Problem):
    """
    Solution for https://adventofcode.com/2020/day/5
    """

    def __init__(self):
        Problem.__init__(self)

    def find_seat(self, line) -> tuple:
        row_lower = 0
        row_upper = 127
        col_lower = 0
        col_upper = 7
        for i in range(0, 10):
            char = line[i]
            if i < 7:
                current_diff = row_upper - row_lower
                if char == 'F':
                    row_upper = row_upper - (math.ceil(current_diff / 2))
                elif char == 'B':
                    row_lower = row_lower + (math.ceil(current_diff / 2))
            else:
                current_diff = col_upper - col_lower
                if char == 'L':
                    col_upper = col_upper - (math.ceil(current_diff / 2))
                elif char == 'R':
                    col_lower = col_lower + (math.ceil(current_diff / 2))

        assert(row_lower == row_upper)
        assert(col_lower == col_upper)
        seat_id = row_lower * 8 + col_lower
        return (row_lower, col_lower, seat_id)

    def solve_a(self) -> int:
        highest_seat_id = 0
        for line in self.input:
            (_, _, seat_id) = self.find_seat(line)
            if seat_id > highest_seat_id:
                highest_seat_id = seat_id

        print(f"The highest seat id is {highest_seat_id}")

    def solve_b(self) -> int:
        seat_ids = []
        for line in self.input:
            (_, _, seat_id) = self.find_seat(line)
            seat_ids.append(seat_id)
        seat_ids.sort()
        for i in range(0, len(seat_ids)):
            if i == (len(seat_ids) - 1):
                continue
            next_expected_id = seat_ids[i] + 1
            if seat_ids[i + 1] != next_expected_id:
                print(f"The seat with ID {next_expected_id} is missing")

    @property
    def name(self) -> str:
        return "Day 5: Binary Boarding"

    @property
    def number(self) -> int:
        return 5
