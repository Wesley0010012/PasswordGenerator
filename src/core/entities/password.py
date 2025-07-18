from .rule import Rule
from typing import List
from .strength import Strength


class Password:
    def __init__(self, length: int, rules: Rule):
        self._length = length
        self._rules = rules
        self._value: str = ""
        self._strength: Strength

    def get_length(self) -> int:
        return self._length

    def get_simplified_value_length(self) -> int:
        return len(set(self._value))

    def add_letter(self, letter: str) -> None:
        self._value += letter

    def set_strength(self, strength: Strength) -> None:
        self._strength = strength

    def get_strength(self) -> Strength:
        return self._strength

    def update_letter(self, letter: str, position: int) -> None:
        self._value = self._value[:position] + letter + self._value[position + 1 :]

    def get_value_length(self) -> int:
        return self._value.__len__()

    def get_value(self) -> str:
        return self._value

    def get_rules(self) -> List[Rule]:
        return self._rules
