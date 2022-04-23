import trio
import trio.testing

from wfc._model import make_grid, iter_neighbors, ADJACENCIES
from wfc.main import run


def test_wfc() -> None:
    nx = ny = 5
    grid = make_grid(nx, ny)

    clock = trio.testing.MockClock(autojump_threshold=0)
    trio.run(run, grid, nx, ny, clock=clock)

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            (module,) = cell.modules
            for ni, nj in iter_neighbors(i, j, nx, ny):
                ncell = grid[ni][nj]
                (nmodule,) = ncell.modules
                assert nmodule in ADJACENCIES[module]
