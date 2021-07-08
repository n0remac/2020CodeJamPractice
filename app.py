from rich.layout import Layout
from rich.live import Live

from panels.cameron import cameron_panel
from panels.antsthebul import ants_panel


def update_layout(layout):
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
    setup(main_layout)
    with Live(main_layout, refresh_per_second=10, screen=True):
        while True:
            update_layout(main_layout)
