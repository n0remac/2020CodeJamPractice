from rich import panel
from rich.text import Text
from rich.panel import Panel


def isaac_panel():
    inner_text = Text(text="Hello everyone", style="bold cyan")
    return Panel(inner_text, title="Isaac", height=3, width=20)
