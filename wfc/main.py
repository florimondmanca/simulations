import itertools
import random
from functools import partial

import trio

from ._display import ShowFunc, make_show, show_nothing
from ._model import (
    collapse_random,
    is_fully_collapsed,
    make_grid,
    pick_random_lowest_entropy_cell,
    propagate,
)
from ._types import Grid


async def _run(grid: Grid, nx: int, ny: int, show: ShowFunc) -> None:
    await show(grid, title="Etat initial", sleep=2)

    i, j = (random.randint(0, nx - 1), random.randint(0, ny - 1))

    for k in itertools.count(1):
        _step_show = partial(show, title=f"Etape {k}")

        collapse_random(grid, i, j)
        await _step_show(grid, sleep=0.3)

        await propagate(
            grid, i, j, nx, ny, checkpoint=partial(_step_show, grid, sleep=0.05)
        )
        await _step_show(grid, sleep=0.3)

        if is_fully_collapsed(grid):
            break

        i, j = pick_random_lowest_entropy_cell(grid)


async def run(grid: Grid, nx: int, ny: int) -> None:
    async with make_show() as show:
        await _run(grid, nx, ny, show=show)

        await show(grid)


if __name__ == "__main__":
    NX = NY = 25
    GRID = make_grid(NX, NY)
    trio.run(run, GRID, NX, NY)
