from src.dgol_worker.cell import Cell


class TestCell:
    def test_repr(self):
        expected = "Cell([1, -3], CellState.DEAD)"
        assert repr(Cell([1, -3])) == expected

    def test_eq(self):
        assert Cell((0, 1)) == Cell((0, 1))

    def test_hash(self):
        # If this throws an error, Cell objects are not hashable
        {Cell((0, 0)), Cell((0, 1))}
