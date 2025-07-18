from ...protocols.i_strategy import IStrategy
from ...protocols.math import Math
from ...entities.password import Password
from ...entities.rule import Rule


class SelectRandomRule(IStrategy[Password, Rule]):
    def __init__(self, math: Math):
        super().__init__()
        self._math = math

    def execute(self, input: Password) -> Rule:
        rules = input.get_rules()

        return rules[self._math.generate_random_number(0, rules.__len__() - 1)]
