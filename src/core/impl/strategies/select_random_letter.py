from ...protocols.i_strategy import IStrategy
from ...protocols.math import Math
from ...entities.rule import Rule


class SelectRandomLetter(IStrategy[Rule, str]):
    def __init__(self, math: Math):
        super().__init__()
        self._math = math

    def execute(self, input: Rule) -> str:
        return input.get_rule_letter(
            self._math.generate_random_number(0, input.get_length() - 1)
        )
