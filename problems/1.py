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
        Find three numbers in the input that add up to 2020 and multiply them.
        """
        pass

    @property
    def name(self) -> str:
        return "Day 1: Sonar Sweep"

    @property
    def number(self) -> int:
        return 1