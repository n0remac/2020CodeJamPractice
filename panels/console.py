from rich.text import Text
from rich.panel import Panel


def console_panel():
    name = Text("console", style="italic green")
    return Panel(name, width=len("console") + 4, height=3)
