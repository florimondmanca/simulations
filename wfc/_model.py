import random
from typing import Awaitable, Callable, Iterator

from ._types import Grid, Cell

ADJACENCIES = {
    "🌳": {"🌳", "🌿"},
    "🌿": {"🌳", "🌿", "🐚"},
    "🐚": {"🌿", "🐚", "🌊"},
    "🌊": {"🐚", "🌊"},
}


def make_grid(nx: int, ny: int) -> Grid:
    grid: Grid = []

    for _ in range(nx):
        row = []
        for _ in range(ny):
            row.append(Cell(set(ADJACENCIES)))
        grid.append(row)

    return grid


def collapse_random(grid: Grid, i: int, j: int) -> None:
    grid[i][j].modules = {random.choice(list(grid[i][j].modules))}


def is_fully_collapsed(grid: Grid) -> bool:
    return all(len(cell.modules) == 1 for row in grid for cell in row)


def iter_neighbors(i: int, j: int, nx: int, ny: int) -> Iterator[tuple[int, int]]:
    if j + 1 < ny:
        yield (i, j + 1)
    if j - 1 >= 0:
        yield (i, j - 1)
    if i + 1 < nx:
        yield (i + 1, j)
    if i - 1 >= 0:
        yield (i - 1, j)


async def propagate(
    grid: Grid,
    i: int,
    j: int,
    nx: int,
    ny: int,
    *,
    checkpoint: Callable[[], Awaitable[None]]
) -> None:
    cell = grid[i][j]
    for ni, nj in iter_neighbors(i, j, nx, ny):
        ncell = grid[ni][nj]
        constraint = set()
        for module in cell.modules:
            constraint |= ADJACENCIES[module]

        if ncell.modules <= constraint:
            continue

        ncell.propagating = True
        ncell.modules &= constraint

        await checkpoint()
        await propagate(grid, ni, nj, nx, ny, checkpoint=checkpoint)
        ncell.propagating = False


def pick_random_lowest_entropy_cell(grid: Grid) -> tuple[int, int]:
    # NOTE: entropy = number of possible states
    candidates = []
    lowest_entropy = float("inf")

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            entropy = len(cell.modules)

            if entropy == 1:
                # This cell has already collasped
                continue

            if entropy == lowest_entropy:
                candidates.append((i, j))
                continue

            if 1 < entropy < lowest_entropy:
                candidates = [(i, j)]
                lowest_entropy = entropy

    assert lowest_entropy < float("inf")
    assert candidates

    return random.choice(candidates)
