import zmq
from ..dgol_worker.cell import Cell
from ..dgol_support import CellState


class CellEnv:
    def __init__(self):
        self.positions = set()
        # Map positions to Cell objects
        self.cells = dict()

    def __repr__(self):
        return "\n".join([repr(c) for c in self.cells])

    def create_cell(self, position, state=CellState.DEAD):
        if position not in self.positions:
            self.positions.add(position)
            self.cells[position] = Cell(position, state)

    def delete_cell(self, position):
        if position in self.positions:
            self.positions.remove(position)
            del self.cells[position]
