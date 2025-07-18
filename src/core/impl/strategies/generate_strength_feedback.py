from ...entities.strength import Strength
from ...protocols.i_strategy import IStrategy
from ...enums.strength_feedback_enum import StrengthFeedbackEnum


class GenerateStrengthFeedback(IStrategy[Strength, None]):
    def execute(self, input: Strength) -> None:
        thresholds = [
            (28, StrengthFeedbackEnum.VERY_POOR),
            (36, StrengthFeedbackEnum.POOR),
            (60, StrengthFeedbackEnum.MEDIUM),
            (128, StrengthFeedbackEnum.GOOD),
        ]

        val = input.get_value()

        feedback = next(
            (feedback for limit, feedback in thresholds if val < limit),
            StrengthFeedbackEnum.GREAT,
        )

        input.set_feedback(feedback)

        return None
