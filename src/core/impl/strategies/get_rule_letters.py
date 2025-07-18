from ...protocols.i_strategy import IStrategy
from ...enums.password_options_enum import PasswordOptionsEnum
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


class GetRuleLetters(IStrategy[PasswordOptionsEnum, str]):
    def __init__(self):
        super().__init__()
        self._option_letters = {
            PasswordOptionsEnum.LOWERCASE: ascii_lowercase,
            PasswordOptionsEnum.UPPERCASE: ascii_uppercase,
            PasswordOptionsEnum.DIGITS: digits,
            PasswordOptionsEnum.SPECIAL_CHARACTERS: punctuation,
        }

    def execute(self, input: PasswordOptionsEnum) -> str:
        return self._option_letters[input]
