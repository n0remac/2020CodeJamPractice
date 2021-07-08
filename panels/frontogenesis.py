from rich.panel import Panel
from rich.text import Text


def frontogenesis_panel():
    text_to_add = Text(text='Frontogenesis has appeared!'.center(3),style='bold magenta')
    return Panel(text_to_add, title='A wild..',width=20,height=4)