from ...protocols.i_strategy import IStrategy
from ...enums.password_options_enum import PasswordOptionsEnum


class VerifyExistentRule(IStrategy[str, None]):
    def execute(self, input):
        if not input in PasswordOptionsEnum.__members__:
            raise AssertionError(f"Cannot find rule with name: {input}")

        return None
