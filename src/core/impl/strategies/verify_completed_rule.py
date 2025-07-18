from ..dto.verify_completed_rule_input_dto import VerifyCompletedRuleInputDto
from ...protocols.i_strategy import IStrategy


class VerifyCompletedRule(IStrategy[VerifyCompletedRuleInputDto, bool]):
    def execute(self, input: VerifyCompletedRuleInputDto) -> bool:
        password = input.get_password()

        rule = input.get_rule()

        return any(letter in rule.get_letters() for letter in password.get_value())
