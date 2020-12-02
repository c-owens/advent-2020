from .problem import Problem

class Day1(Problem):
    """
    Solution for https://adventofcode.com/2020/day/1
    """

    def __init__(self):
        Problem.__init__(self)
        
        # Convert the input lines to integers
        self.input_ints = []
        for i in range(0, len(self.input)):
            self.input_ints.append(int(self.input[i]))

        # Also store them as a set
        self.input_set = set(self.input_ints)

    def solve_a(self) -> int:
        """
        Find two numbers in the input that add up to 2020 and multiply them.
        """
        goal_sum = 2020
        for current_num in self.input_set:
            desired_num = goal_sum - current_num
            if desired_num in self.input_set:
                print( f"{current_num} + {desired_num} = {goal_sum}" )
                solution = current_num * desired_num
                print( f"{current_num} * {desired_num} = {solution}" )
                return solution

    def solve_b(self) -> int:
        """
        Find three numbers in the input that add up to 2020 and multiply them.
        """
        goal_sum = 2020
        # Use the outer loop to track our first number
        for idx1 in range(0, len(self.input_ints)):
            first_num = self.input_ints[idx1]

            # And an inner loop to track the second number
            for idx2 in range(0, len(self.input_ints)):
                # Don't evaluate the first number
                if idx2 == idx1:
                    continue

                # Find the third number in the set that gets us to the goal sum
                second_num = self.input_ints[idx2]
                current_sum = first_num + second_num
                desired_num = goal_sum - current_sum
                if desired_num in self.input_set:
                    print( f"{first_num} + {second_num} + {desired_num} = {goal_sum}" )
                    solution = first_num * second_num * desired_num
                    print( f"{first_num} * {second_num} * {desired_num} = {solution}" )
                    return solution

    @property
    def name(self) -> str:
        return "Day 1: Report Repair"

    @property
    def number(self) -> int:
        return 1