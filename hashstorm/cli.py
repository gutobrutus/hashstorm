import time
from typer import Argument, Typer, Option, Exit
from typing import Optional
from rich import print
from hashstorm.banner import show_banner
from hashstorm.config import help_text
from hashstorm.core import process_wordlist

main = Typer(
    help='HashStorm - Hash Decrypter App',
    context_settings={"help_option_names": ["-h", "--help"]},
    add_completion=False,
)

__version__ = help_text['VERSION']

show_banner()


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
    start_time = time.time()
    print('Iniciando o processamento em {}'.format(time.ctime()))
    process_wordlist(wordlist, hash_target, algorithms)
    print('Tempo total: {:.3f} seconds'.format(time.time() - start_time))
