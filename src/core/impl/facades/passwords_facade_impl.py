from ...protocols.passwords_facade import PasswordsFacade
from ...protocols.i_strategy import IStrategy
from typing import List
from ...entities.rule import Rule
from ...entities.password import Password
from ..dto.create_password_input_dto import CreatePasswordInputDto


class PasswordsFacadeImpl(PasswordsFacade):
    def __init__(
        self,
        create_rules: IStrategy[List[str], List[Rule]],
        create_password_entity: IStrategy[List[Rule], Password],
        generate_password: IStrategy[Password, None],
        fill_minimum_rules: IStrategy[Password, None],
        define_password_strength: IStrategy[Password, None],
    ):
        super().__init__()
        self._create_rules = create_rules
        self._create_password_entity = create_password_entity
        self._generate_password = generate_password
        self._fill_minimum_rules = fill_minimum_rules
        self._define_password_strength = define_password_strength

    def generate_password(self, length: int, options: List[str]) -> Password:
        rules = self._create_rules.execute(options)
        password = self._create_password_entity.execute(
            CreatePasswordInputDto(length, rules)
        )
        self._generate_password.execute(password)
        self._fill_minimum_rules.execute(password)
        self._define_password_strength.execute(password)

        return password
