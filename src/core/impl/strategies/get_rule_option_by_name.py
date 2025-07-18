from ...protocols.i_strategy import IStrategy
from ...enums.password_options_enum import PasswordOptionsEnum


class GetRuleOptionByName(IStrategy[str, None]):
    def execute(self, input):
        return PasswordOptionsEnum[input]
