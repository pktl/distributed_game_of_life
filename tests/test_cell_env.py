from src.dgol_worker.cell_env import CellEnv
from src.dgol_worker.cell import Cell
from src.dgol_support import CellState


class TestCellEnv:
    def test_create_cell(self):
        ce = CellEnv()
        ce.create_cell((0, 0))
        ce.create_cell((0, 1), CellState.ALIVE)
        expected_cells = {
            (0, 0): Cell((0, 0), CellState.DEAD),
            (0, 1): Cell((0, 1), CellState.ALIVE)}
        expected_positions = {(0, 0), (0, 1)}
        assert ce.cells == expected_cells
        assert ce.positions == expected_positions

    def test_delete_cell(self):
        ce = CellEnv()
        ce.create_cell((0, 0))
        ce.create_cell((0, 1), CellState.ALIVE)
        ce.delete_cell((0, 1))
        expected_cells = {
            (0, 0): Cell((0, 0), CellState.DEAD)}
        expected_positions = {(0, 0)}
        assert ce.cells == expected_cells
        assert ce.positions == expected_positions
