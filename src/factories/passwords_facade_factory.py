from src.core.protocols.factory import Factory
from src.core.protocols.passwords_facade import PasswordsFacade
from src.core.impl.facades.passwords_facade_impl import PasswordsFacadeImpl
from src.core.impl.strategies.create_password_entity import CreatePasswordEntity
from src.core.impl.strategies.create_rules import CreateRules
from src.core.impl.strategies.generate_password import GeneratePassword
from src.infra.math.default_math import DefaultMath
from src.core.impl.strategies.select_random_rule import SelectRandomRule
from src.core.impl.strategies.select_random_letter import SelectRandomLetter
from src.core.impl.strategies.fill_minimum_rules import FillMinimumRules
from src.core.impl.strategies.verify_completed_rule import VerifyCompletedRule
from src.core.impl.strategies.update_random_letter import UpdateRandomLetter
from src.core.impl.strategies.calculate_password_strength import (
    CalculatePasswordStrength,
)
from src.core.impl.strategies.create_rule import CreateRule
from src.core.impl.strategies.verify_existent_rule import VerifyExistentRule
from src.core.impl.strategies.get_rule_letters import GetRuleLetters
from src.core.impl.strategies.get_rule_option_by_name import GetRuleOptionByName
from src.core.impl.strategies.get_total_rules_chars import GetTotalRulesChars
from src.core.impl.strategies.generate_strength_feedback import GenerateStrengthFeedback


class PasswordsFacadeFactory(Factory[None, PasswordsFacade]):
    def build(input: None) -> PasswordsFacade:
        math = DefaultMath()
        select_random_rule = SelectRandomRule(math)
        select_random_letter = SelectRandomLetter(math)
        update_random_letter = UpdateRandomLetter(math, select_random_letter)
        verify_existent_rule = VerifyExistentRule()
        get_rule_option_by_name = GetRuleOptionByName()
        get_rule_letters = GetRuleLetters()
        create_rule = CreateRule(
            verify_existent_rule, get_rule_option_by_name, get_rule_letters
        )
        get_total_rules_chars = GetTotalRulesChars()
        generate_strength_feedback = GenerateStrengthFeedback()

        return PasswordsFacadeImpl(
            CreateRules(create_rule),
            CreatePasswordEntity(),
            GeneratePassword(select_random_rule, select_random_letter),
            FillMinimumRules(VerifyCompletedRule(), update_random_letter),
            CalculatePasswordStrength(
                math, get_total_rules_chars, generate_strength_feedback
            ),
        )
