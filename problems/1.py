from .problem import Problem

class Day1(Problem):
    """
    Solution for https://adventofcode.com/2021/day/1
    """

    def __init__(self):
        Problem.__init__(self)
        
        # Convert the input lines to integers
        self.input_ints = []
        for i in range(0, len(self.input)):
            self.input_ints.append(int(self.input[i]))

    def solve_a(self) -> int:
        """
        Count the number of cases where an integer is larger than the previous value
        """
        previous_num = None
        increase_count = 0
        for current_num in self.input_ints:
            if previous_num is None:
                previous_num = current_num
                continue
            if current_num > previous_num:
                increase_count += 1
            previous_num = current_num
        print( f"Number of depth increases = {increase_count}")
        return increase_count

    def solve_b(self) -> int:
        """
        Sum every group of 3 numbers in the list and then count the cases where the sum is larger than the previous sum
        """
        previous_sum = None
        increase_count = 0
        for i in range(0, len(self.input_ints) - 2):
            num_one = self.input_ints[i]
            num_two = self.input_ints[i+1]
            num_three = self.input_ints[i+2]
            total = num_one + num_two + num_three
            if previous_sum is not None and total > previous_sum:
                increase_count += 1
            previous_sum = total
        print( f"Number of sliding depth increases = {increase_count}")
        return increase_count

    @property
    def name(self) -> str:
        return "Day 1: Sonar Sweep"

    @property
    def number(self) -> int:
        return 1