from src.core.protocols.math import Math
from random import randint
from math import log2


class DefaultMath(Math):
    def generate_random_number(self, min, max):
        return randint(min, max)

    def calculate_uniform_entropy(
        self, event_length: int, number_of_occurences: int
    ) -> float:
        return log2(event_length) * number_of_occurences
