from rich.text import Text
from rich.panel import Panel


def free_panel():
    name = Text("free", style="bold green")
    return Panel(name, width=12, height=3)
