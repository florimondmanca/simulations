import pytest

from wfc.main import run, make_grid, iter_neighbors, show, ADJACENCIES


def test_wfc(capsys: pytest.CaptureFixture) -> None:
    nx = ny = 5
    grid = make_grid(nx, ny)

    run(grid, nx, ny)
    show(grid)

    captured = capsys.readouterr()
    modules = set(captured.out) - {"\n", " "}
    assert modules <= {"🌳", "🌿", "🐚", "🌊"}
    assert len(modules) >= 2

    for i, row in enumerate(grid):
        for j, (module,) in enumerate(row):
            for ni, nj in iter_neighbors(i, j, nx, ny):
                n_module, = grid[ni][nj]
                assert n_module in ADJACENCIES[module]
