from abc import ABC, abstractmethod
from typing import Generic, TypeVar

Input = TypeVar("Input")
Output = TypeVar("Output")


class Factory(ABC, Generic[Input, Output]):
    @abstractmethod
    def build(input: Input) -> Output:
        pass
