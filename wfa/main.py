from typing import Iterator
import random

Grid = list[list[set[str]]]

ADJACENCIES = {
    "🌳": {"🌳", "🌿"},
    "🌿": {"🌳", "🌿", "🐚"},
    "🐚": {"🌿", "🐚", "🌊"},
    "🌊": {"🐚", "🌊"},
}

MODULES = set(ADJACENCIES)


def make_grid(nx: int, ny: int) -> Grid:
    grid: Grid = []

    for _ in range(nx):
        row = []
        for _ in range(ny):
            row.append(set(ADJACENCIES))
        grid.append(row)

    return grid


def show(grid: Grid) -> None:
    lines = []
    for row in grid:
        line = ""
        for modules in row:
            if len(modules) == 1:
                (module,) = modules
                line += format(module, "2s")
            else:
                line += format(str(len(modules)), "3s")
        lines.append(line)

    print("\n".join(lines))


def collapse_random(grid: Grid, i: int, j: int) -> None:
    grid[i][j] = {random.choice(list(grid[i][j]))}


def is_fully_collapsed(grid: Grid) -> bool:
    return all(len(modules) == 1 for row in grid for modules in row)


def iter_neighbors(i: int, j: int, nx: int, ny: int) -> Iterator[tuple[int, int]]:
    if j + 1 < ny:
        yield (i, j + 1)
    if j - 1 >= 0:
        yield (i, j - 1)
    if i + 1 < nx:
        yield (i + 1, j)
    if i - 1 >= 0:
        yield (i - 1, j)


def propagate(grid: Grid, i: int, j: int, nx: int, ny: int) -> None:
    for ni, nj in iter_neighbors(i, j, nx, ny):
        constraint = set()
        for module in grid[i][j]:
            constraint |= ADJACENCIES[module]

        if grid[ni][nj] <= constraint:
            continue

        grid[ni][nj] &= constraint
        propagate(grid, ni, nj, nx, ny)


def pick_random_lowest_entropy_cell(grid: Grid) -> tuple[int, int]:
    # NOTE: entropy = number of possible states
    candidates = []
    lowest_entropy = float("inf")

    for i, row in enumerate(grid):
        for j, modules in enumerate(row):
            entropy = len(modules)

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


def run(grid: Grid, nx: int, ny: int) -> None:
    i, j = (random.randint(0, nx - 1), random.randint(0, ny - 1))

    while True:
        collapse_random(grid, i, j)
        propagate(grid, i, j, nx, ny)

        if is_fully_collapsed(grid):
            break

        i, j = pick_random_lowest_entropy_cell(grid)


if __name__ == "__main__":
    NX = NY = 25
    GRID = make_grid(NX, NY)
    run(GRID, NX, NY)
    show(GRID)
