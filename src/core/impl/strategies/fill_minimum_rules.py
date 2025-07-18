from ...entities.password import Password
from ...entities.rule import Rule
from ...entities.password import Password
from ...protocols.i_strategy import IStrategy
from ..dto.verify_completed_rule_input_dto import VerifyCompletedRuleInputDto
from ..dto.update_random_letter_input_dto import UpdateRandomLetterInputDto


class FillMinimumRules(IStrategy[Password, None]):
    def __init__(
        self,
        verify_completed_rule: IStrategy[Rule, str],
        update_random_letter: IStrategy[Rule, str],
    ):
        self._verify_completed_rule = verify_completed_rule
        self._update_random_letter = update_random_letter

    def execute(self, input: Password) -> None:
        for rule in input.get_rules():
            if not self._verify_completed_rule.execute(
                VerifyCompletedRuleInputDto(input, rule)
            ):
                self._update_random_letter.execute(
                    UpdateRandomLetterInputDto(input, rule)
                )

        return None
