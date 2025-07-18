from ...protocols.i_strategy import IStrategy
from ...entities.password import Password


class GetTotalRulesChars(IStrategy[Password, int]):
    def execute(self, input: Password) -> int:
        return sum(rule.get_length() for rule in input.get_rules())
