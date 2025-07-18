from abc import ABC, abstractmethod
from typing import Generic, TypeVar

Input = TypeVar("Input")
Output = TypeVar("Output")


class IStrategy(ABC, Generic[Input, Output]):
    @abstractmethod
    def execute(input: Input) -> Output:
        pass
