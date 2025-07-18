from ...protocols.i_strategy import IStrategy
from ...entities.rule import Rule
from typing import List
from ...enums.password_options_enum import PasswordOptionsEnum


class CreateRules(IStrategy[List[str], List[Rule]]):
    def __init__(self, create_rule: IStrategy[str, Rule]):
        super().__init__()
        self._create_rule = create_rule

    def execute(self, input: List[str]) -> List[Rule]:
        rules = []

        for option in input:
            rules.append(self._create_rule.execute(option))

        return rules
