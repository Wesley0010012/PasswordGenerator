from ..enums.password_options_enum import PasswordOptionsEnum


class Rule:
    def __init__(self, option: PasswordOptionsEnum, letters: str):
        self._option = option
        self._letters = letters

    def get_option(self) -> PasswordOptionsEnum:
        return self._option

    def get_length(self) -> int:
        return self._letters.__len__()

    def get_letters(self) -> str:
        return self._letters

    def get_rule_letter(self, index: int) -> str:
        return self._letters[index]
