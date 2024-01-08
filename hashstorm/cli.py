from typer import Argument, Typer, Option, Exit
from typing import Optional
from rich import print
from hashstorm.config import help_text
from hashstorm.core import process_wordlist

main = Typer(
    help='Hash Decoder App',
    context_settings={"help_option_names": ["-h", "--help"]},
    add_completion=False,
)

__version__ = help_text['VERSION']


def version_callback(value: bool):
    if value:
        print(f'HashStorm CLI Version: {__version__}')
        raise Exit(code=0)


@main.command()
def run_app(
        wordlist: str = Argument(..., metavar='wordlist', help=help_text['WORDLIST']),
        hash_target: str = Argument(..., metavar='hash_target', help=help_text['HASH']),
        algorithms: str = Argument(..., metavar='algorítmos', help=help_text['ALGORITHMS']),
        version: Optional[bool] = Option(
            None, '--version', '-v', help='Show version app', callback=version_callback
        ),
):
    print('Inificiando o processamento...')
    process_wordlist(wordlist, hash_target, algorithms)
