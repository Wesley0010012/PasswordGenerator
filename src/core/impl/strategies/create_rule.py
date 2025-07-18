from ...protocols.i_strategy import IStrategy
from ...entities.rule import Rule
from ...enums.password_options_enum import PasswordOptionsEnum


class CreateRule(IStrategy[str, Rule]):
    def __init__(
        self,
        verify_existent_rule: IStrategy[str, None],
        get_rule_option_by_name: IStrategy[str, PasswordOptionsEnum],
        get_rule_letters: IStrategy[PasswordOptionsEnum, str],
    ):
        super().__init__()
        self._verify_existent_rule = verify_existent_rule
        self._get_rule_option_by_name = get_rule_option_by_name
        self._get_rule_letters = get_rule_letters

    def execute(self, input: str) -> str:
        input = input.upper()
        self._verify_existent_rule.execute(input)

        rule_option = self._get_rule_option_by_name.execute(input)

        return Rule(rule_option, self._get_rule_letters.execute(rule_option))
