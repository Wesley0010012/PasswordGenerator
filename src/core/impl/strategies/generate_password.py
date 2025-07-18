from ...entities.password import Password
from ...entities.rule import Rule
from ...entities.password import Password
from ...protocols.i_strategy import IStrategy


class GeneratePassword(IStrategy[Password, None]):
    def __init__(
        self,
        select_random_rule: IStrategy[Password, Rule],
        select_random_letter: IStrategy[Rule, str],
    ):
        self._select_random_rule = select_random_rule
        self._select_random_letter = select_random_letter

    def execute(self, input: Password) -> None:
        for _ in range(input.get_length()):
            input.add_letter(
                self._select_random_letter.execute(
                    self._select_random_rule.execute(input)
                )
            )

        return None
