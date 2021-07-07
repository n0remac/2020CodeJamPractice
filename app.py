from rich.layout import Layout
from rich.live import Live

from panels.cameron import cameron_panel


def run_app(layout):
    layout["right"].update(cameron_panel())


def setup(layout):
    layout.split_column(
        Layout(name="right"),
        Layout(name="left"),
    )


main_layout = Layout()

if __name__ == "__main__":
    setup(main_layout)
    with Live(main_layout, refresh_per_second=10, screen=True):
        while True:
            run_app(main_layout)
