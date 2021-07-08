from rich.text import Text
from rich.panel import Panel


def ants_panel():
    name = Text("Antsthebul", style="bold red on white")
    return Panel(name, title="Hello, I am", width=len(name) + 4, height=3)
