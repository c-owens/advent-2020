"""
The abstract base class for problems.
"""
import os
from abc import ABC, abstractmethod
from typing import List

class Problem(ABC):

    def __init__(self):
        self.input = self.load_input()

    @abstractmethod
    def solve_a(self) -> None:
        pass

    @abstractmethod
    def solve_b(self) -> None:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def number(self) -> int:
        pass

    def load_input(self) -> List[str]:
        input_file = os.path.join(os.path.dirname(__file__), "..", "input", f"input{self.number}.txt")
        with open(input_file) as file:
            return file.read().splitlines()