from pyfiglet import Figlet
from rich import print
from hashstorm.config import help_text


def show_banner():
    f = Figlet(font='big', justify='right', width=80)
    art_text = f.renderText('HashStorm')
    print('=' * 80)
    print(f'[bold yellow]{art_text}[/bold yellow]', end='')
    print(' ' * 25, 'Doc/Repo: {}'.format(help_text['DOC']))
    print('=' * 80)
