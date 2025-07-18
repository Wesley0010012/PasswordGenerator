from src.factories.passwords_facade_factory import PasswordsFacadeFactory
from src.core.enums.password_options_enum import PasswordOptionsEnum
from src.core.entities.password import Password

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

import argparse

from pyfiglet import Figlet

parser = argparse.ArgumentParser("./password_generator")
parser.add_argument(
    "-l",
    "--lowercase",
    action="store_const",
    const=PasswordOptionsEnum.LOWERCASE,
    required=False,
)
parser.add_argument(
    "-u",
    "--uppercase",
    action="store_const",
    const=PasswordOptionsEnum.UPPERCASE,
    required=False,
)
parser.add_argument(
    "-d",
    "--digits",
    action="store_const",
    const=PasswordOptionsEnum.DIGITS,
    required=False,
)
parser.add_argument(
    "-sc",
    "--special-characters",
    action="store_const",
    const=PasswordOptionsEnum.SPECIAL_CHARACTERS,
    required=False,
)
parser.add_argument("-s", "--size", type=int, required=True)

console = Console()

figlet = Figlet(font="slant")
ascii_art = figlet.renderText("Password\nGenerator")

console.print(
    Panel(
        f"[bold cyan]{ascii_art}[/bold cyan]",
        border_style="magenta",
        subtitle="[magenta]by Wesley0010012[/magenta]",
        expand=True,
    )
)
print()

args = parser.parse_args()

option_values = [args.lowercase, args.uppercase, args.digits, args.special_characters]


def print_password_info(password: Password) -> None:
    table = Table(show_header=False, box=box.SQUARE, expand=True)
    table.add_row("Password:", str(password.get_value()))
    table.add_row("Length:", str(password.get_length()))
    table.add_row("Entropy:", f"{password.get_strength().get_value():.10f} bits")
    table.add_row("Feedback:", password.get_strength().get_feedback().value)

    panel = Panel(table, title="Password Generated Info", border_style="green")

    console.print(panel)


if not all(v is None for v in option_values):
    facade = (PasswordsFacadeFactory()).build()

    selected_options = [v.value for v in option_values if v is not None]
    password = facade.generate_password(args.size, selected_options)

    print_password_info(password)
else:
    parser.print_help()
