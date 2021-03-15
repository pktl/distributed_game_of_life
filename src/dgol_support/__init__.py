from enum import Enum


class CellState(Enum):
    ALIVE = True
    DEAD = False

    def __str__(self):
        if self == CellState.ALIVE:
            return "alive"
        else:
            return "dead"

    def __repr__(self):
        return f"CellState.{self.name}"
