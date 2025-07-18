from ...entities.password import Password
from ...entities.rule import Rule


class UpdateRandomLetterInputDto:
    def __init__(self, password: Password, rule: Rule):
        self._password = password
        self._rule = rule

    def get_password(self) -> Password:
        return self._password

    def get_rule(self) -> Rule:
        return self._rule
