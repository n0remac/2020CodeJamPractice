from rich.text import Text
from rich.panel import Panel


def cameron_panel():
    name = Text("cameron", style="bold blue")
    return Panel(name, width=12, height=3)
