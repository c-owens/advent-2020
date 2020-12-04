
from .problem import Problem
import re

class Day4(Problem):
    """
    Solution for https://adventofcode.com/2020/day/4
    """

    def __init__(self):
        Problem.__init__(self)

    def validate_year(self, year_str: str, min: int, max: int) -> bool:
        try:
            year = int(year_str)
        except:
            return False
        return year >= min and year <= max

    def validate_height(self, height_str: str) -> bool:
        if not height_str:
            return False

        try:
            measurement = height_str[-2:]
            height = int(height_str.rstrip(measurement))
        except:
            return False

        if measurement == 'cm':
            return height >= 150 and height <= 193
        elif measurement == 'in':
            return height >= 59 and height <= 76
        else:
            return False

    def validate_expression(self, input_str: str, expression: str) -> bool:
        if not input_str:
            return False

        match = re.search(expression, input_str)
        return match != None

    def record_is_valid(self, record: dict, validate_value: bool=False) -> bool:
        required_fields_exist = (
            'byr' in record and
            'iyr' in record and
            'eyr' in record and
            'hgt' in record and
            'hcl' in record and
            'ecl' in record and
            'pid' in record)
        
        if not required_fields_exist:
            return False
        if not validate_value:
            return True

        return (
            self.validate_year(record['byr'], 1920, 2002) and
            self.validate_year(record['iyr'], 2010, 2020) and
            self.validate_year(record['eyr'], 2020, 2030) and
            self.validate_height(record['hgt']) and
            self.validate_expression(record['hcl'], r"^#[0-9a-f]{6}$") and
            self.validate_expression(record['ecl'], r"^(amb|blu|brn|gry|grn|hzl|oth)$") and
            self.validate_expression(record['pid'], r"^[\d]{9}$"))

    def count_valid_inputs(self, validate_values: bool=False) -> int:
        # Add a blank line to the end so our loop sees this as the end of an entry
        input_padded = self.input
        input_padded.append( '' )

        num_valid = 0
        current_record = {}
        for line in input_padded:
            if not line:
                # We're done with the previous record
                if self.record_is_valid(current_record, validate_values):
                    num_valid += 1
                current_record = {}
                continue

            sections = line.split(" ")
            for section in sections:
                key_val = section.split(":")
                current_record[key_val[0]] = key_val[1].strip()
        
        return num_valid

    def solve_a(self) -> int:
        num_valid = self.count_valid_inputs()
        print(f"There are {num_valid} valid passport keys in the list")

    def solve_b(self) -> int:
        num_valid = self.count_valid_inputs(validate_values=True)
        print(f"There are {num_valid} valid passport keys and values in the list")

    @property
    def name(self) -> str:
        return "Day 4: Passport Processing"

    @property
    def number(self) -> int:
        return 4
