import zmq
from ..dgol_worker.cell import Cell
from ..dgol_support import CellState


class CellEnv:
    def __init__(self):
        self.positions = set()
        # Map positions to Cell objects
        self.cells = dict()
        self.ctx = zmq.Context()
        self._connect_to_master()

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

    def _connect_to_master(self):
        rep = self.ctx.socket(zmq.REP)
        rep.bind("tcp://*:5555")
        self._recv_loop(rep)

    def _recv_loop(self, reply_socket):
        while True:
            msg = reply_socket.recv_string()
            if msg == "q":
                break
            else:
                self._message_handler(msg)
            reply_socket.send_string("ACK")

    def _message_handler(self, msg):
        print(msg)
