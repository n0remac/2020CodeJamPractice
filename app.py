from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich.panel import Panel

from panels.cameron import cameron_panel
from panels.antsthebul import ants_panel

def run_app(layout):
    pass


def setup(layout):
    layout.split_column(
        Layout(name="top"),
        Layout(name="bottom"),
    )
    layout["top"].split_row(
        Layout(cameron_panel()),
        Layout(ants_panel()))

main_layout = Layout()

if __name__ == "__main__":
    with Live(layout, refresh_per_second=10, screen=True):
        while True:
            run_app(layout)
