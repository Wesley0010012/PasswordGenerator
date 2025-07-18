from abc import ABC, abstractmethod


class Math(ABC):
    @abstractmethod
    def calculate_uniform_entropy(
        event_length: int, number_of_occurences: int
    ) -> float:
        pass

    @abstractmethod
    def generate_random_number(min: int, max: int) -> int:
        pass
