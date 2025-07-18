from ..dto.update_random_letter_input_dto import UpdateRandomLetterInputDto
from ...entities.rule import Rule

from ...protocols.math import Math
from ...protocols.i_strategy import IStrategy


class UpdateRandomLetter(IStrategy[UpdateRandomLetterInputDto, None]):
    def __init__(self, math: Math, select_random_letter: IStrategy[Rule, str]):
        super().__init__()
        self._math = math
        self._select_random_letter = select_random_letter

    def execute(self, input: UpdateRandomLetterInputDto) -> None:
        password = input.get_password()

        password.update_letter(
            self._select_random_letter.execute(input.get_rule()),
            self._math.generate_random_number(0, password.get_length() - 1),
        )

        return None
