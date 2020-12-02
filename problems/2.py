from .problem import Problem
from collections import namedtuple
import re

class Day2(Problem):
    """
    Solution for https://adventofcode.com/2020/day/2
    """

    def __init__(self):
        Problem.__init__(self)

    def parse_password_line(self, line: str) -> tuple:
        Output = namedtuple("Output", ["num1", "num2", "character", "password"])
        expression = r"(?P<num1>\d{1,3})-(?P<num2>\d{1,3}) (?P<character>\w): (?P<password>.+)"
        matches = re.search(expression, line)
        num1 = int(matches.group("num1"))
        num2 = int(matches.group("num2"))
        character = matches.group("character")
        password = matches.group("password")
        return Output(num1, num2, character, password)

    def solve_a(self) -> int:
        """
        Given a list of password policies and passwords, count the number of valid passwords according to the policy
        Example:
        1-3 a: abcde
        The password must contain 1 to 3 occurences of the character "a"
        """
        num_valid = 0
        for line in self.input:
            parsed = self.parse_password_line(line)
            char_count = parsed.password.count(parsed.character)
            if char_count >= parsed.num1 and char_count <= parsed.num2:
                num_valid += 1
        
        print(f"There are {num_valid} valid passwords in the list (out of {len(self.input)} items)")
        return num_valid

    def solve_b(self) -> int:
        """
        Given a list of password policies and passwords, count the number of valid passwords according to the policy
        Example:
        1-3 a: abcde
        The password must contain the character "a" in the first or third position, but not both
        """
        num_valid = 0
        for line in self.input:
            parsed = self.parse_password_line(line)
            # The character has to be in one of these indexes (but not both).
            in_first_pos = parsed.password[parsed.num1 - 1] == parsed.character
            in_second_pos = parsed.password[parsed.num2 - 1] == parsed.character
            if in_first_pos and in_second_pos:
                continue

            if in_first_pos or in_second_pos:
                num_valid += 1
        
        print(f"There are {num_valid} valid passwords in the list (out of {len(self.input)} items)")
        return num_valid

    @property
    def name(self) -> str:
        return "Day 2: Password Philosophy"

    @property
    def number(self) -> int:
        return 2