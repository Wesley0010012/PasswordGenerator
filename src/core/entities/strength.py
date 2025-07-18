from ..enums.strength_feedback_enum import StrengthFeedbackEnum


class Strength:
    def __init__(self, value: float):
        self._value = value
        self._feedback: StrengthFeedbackEnum

    def get_value(self) -> float:
        return self._value

    def set_feedback(self, feedback: StrengthFeedbackEnum) -> None:
        self._feedback = feedback

    def get_feedback(self) -> StrengthFeedbackEnum:
        return self._feedback
