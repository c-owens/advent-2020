"""
Runs setuptools builds for all packages in the repository.
"""

import os
import sys
import subprocess

if __name__ == '__main__':
    # Find the problems directory
    this_dir = os.path.dirname(os.path.realpath(__file__))
    root_dir = os.path.dirname(this_dir)
    problems_dir = os.path.join(root_dir, "problems")

    problem_num = sys.argv[1]
    problem_name = sys.argv[2]

    output_path = os.path.join(problems_dir, f"{problem_num}.py")

file_content = f'''
from .problem import Problem

class Day{problem_num}(Problem):
    """
    Solution for https://adventofcode.com/2020/day/{problem_num}
    """

    def __init__(self):
        Problem.__init__(self)

    def solve_a(self) -> int:
        pass

    def solve_b(self) -> int:
        pass

    @property
    def name(self) -> str:
        return "{problem_name}"

    @property
    def number(self) -> int:
        return {problem_num}
'''

with open(output_path, "w") as file:
    file.write(file_content)