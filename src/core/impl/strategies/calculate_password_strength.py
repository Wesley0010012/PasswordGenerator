from ...protocols.i_strategy import IStrategy
from ...entities.password import Password
from ...protocols.math import Math
from ...entities.strength import Strength


class CalculatePasswordStrength(IStrategy[Password, None]):
    def __init__(
        self,
        math: Math,
        get_total_rules_chars: IStrategy[Password, int],
        generate_strength_feedback: IStrategy[Strength, None],
    ):
        super().__init__()
        self._math = math
        self._get_total_rules_chars = get_total_rules_chars
        self._generate_strength_feedback = generate_strength_feedback

    def __calculate_strength(self, password: Password) -> float:
        return self._math.calculate_uniform_entropy(
            self._get_total_rules_chars.execute(password),
            password.get_simplified_value_length(),
        )

    def execute(self, input: Password) -> None:
        strength = Strength(self.__calculate_strength(input))

        self._generate_strength_feedback.execute(strength)

        input.set_strength(strength)

        return None
