from ...protocols.i_strategy import IStrategy
from ...entities.password import Password
from ..dto.create_password_input_dto import CreatePasswordInputDto


class CreatePasswordEntity(IStrategy[CreatePasswordInputDto, Password]):
    def execute(self, input: CreatePasswordInputDto):
        return Password(input.get_password_length(), input.get_rules())
