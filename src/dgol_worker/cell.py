from ..dgol_support import CellState, Position


class Cell:
    def __init__(self,
                 position: Position,
                 state: CellState = CellState.DEAD):
        self.position = position
        if isinstance(state, CellState):
            self.state = state
        elif isinstance(state, str):
            if state.lower() == "alive":
                self.state = CellState.ALIVE
            elif state.lower() == "dead":
                self.state = CellState.DEAD

    def __repr__(self):
        return f"Cell({repr(self.position)}, {repr(self.state)})"

    # Cells are equal if they occupy the same position
    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)

    def __del__(self):
        pass
