from abc import ABC, abstractmethod
from ..entities.password import Password
from typing import List


class PasswordsFacade:
    @abstractmethod
    def generate_password(length: int, options: List[str]) -> Password:
        pass
