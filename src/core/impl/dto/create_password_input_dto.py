from ...entities.rule import Rule
from typing import List


class CreatePasswordInputDto:
    def __init__(self, password_length: int, rules: List[Rule]):
        self._password_length = password_length
        self._rules = rules

    def get_password_length(self) -> int:
        return self._password_length

    def get_rules(self) -> List[Rule]:
        return self._rules
