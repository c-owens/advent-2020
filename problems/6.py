
from .problem import Problem

class Day6(Problem):
    """
    Solution for https://adventofcode.com/2020/day/6
    """

    def __init__(self):
        Problem.__init__(self)
        self.input.append("")

    def solve_a(self) -> int:
        sum_of_answers = 0
        group = set()
        for line in self.input:
            if not line:
                sum_of_answers += len(group)
                group = set()
                continue
            for char in line:
                group.add(char)

        print(f"Sum of yes answers = {sum_of_answers}")

    def solve_b(self) -> int:
        sum_of_answers = 0
        group_sets = []
        for line in self.input:
            if line:
                group_sets.append(set(line))
            else:
                all_yes = set.intersection(*group_sets)
                sum_of_answers += len(all_yes)
                group_sets = []
        
        print(f"Sum of group wide yes answers = {sum_of_answers}")

    @property
    def name(self) -> str:
        return "Day 6: Custom Customs"

    @property
    def number(self) -> int:
        return 6
