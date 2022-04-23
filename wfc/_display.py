from contextlib import asynccontextmanager
from typing import AsyncIterator, Awaitable, Iterator, Protocol

import trio
from rich.padding import Padding
from rich.live import Live
from rich.panel import Panel
from rich.style import Style

from ._types import Grid

colors = {
    2: "green",
    3: "blue",
    4: "white",
}

style_1 = Style()


class ShowFunc(Protocol):
    def __call__(
        self, grid: Grid, *, title: str = "", sleep: float = 0.0
    ) -> Awaitable[None]:
        ...


def _make_lines(grid: Grid) -> Iterator[str]:
    for row in grid:
        line = "  "

        for cell in row:
            if len(cell.modules) == 1:
                (module,) = cell.modules
                part = f"{module:2s}"
            else:
                n = len(cell.modules)
                part = f"{str(n):3s}"
                if (color := colors.get(n)) is not None:
                    part = f"[{color}]{part}[/]"

            if cell.propagating:
                part = f"[bold]{part}[/]"

            line += part

        yield line


def _make_panel(grid: Grid, title: str = "") -> Panel:
    text = "\n".join(_make_lines(grid))
    return Panel.fit(text, title=title)


@asynccontextmanager
async def make_show() -> AsyncIterator[ShowFunc]:
    with Live(refresh_per_second=4, auto_refresh=True) as liveobj:

        async def _show(grid: Grid, *, title: str = "", sleep: float = 0.0) -> None:
            panel = _make_panel(grid, title=title)
            pad = Padding(panel, (2, 4))
            liveobj.update(pad)
            await trio.sleep(sleep / 20)

        yield _show
        return


async def show_nothing(grid: Grid, *, title: str = "", sleep: float = 0.0) -> None:
    pass
