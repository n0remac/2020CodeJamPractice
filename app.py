from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich.panel import Panel


def run_app(layout):
    pass


layout = Layout()

if __name__ == "__main__":
    with Live(layout, refresh_per_second=10, screen=True):
        while True:
            run_app(layout)
