import zmq
import json
from ..dgol_worker.cell import Cell
from ..dgol_support import CellState


class CellEnv:
    def __init__(self):
        self.positions = set()
        # Map positions to Cell objects
        self.cells = dict()
        self.ctx = zmq.Context()
        self._launch_server()

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

    def _launch_server(self):
        rep = self.ctx.socket(zmq.REP)
        rep.bind("tcp://*:5555")
        self._server_loop(rep)

    def _server_loop(self, reply_socket):
        while True:
            msg = reply_socket.recv_json()
            reply_socket.send_json(self._reply_to(msg))

    def _reply_to(self, msg_json):
        msg_dict = json.loads(msg_json)
        if msg_dict["cmd"] == "create_cell":
            self.create_cell(tuple(msg_dict["args"][0]))
            reply = {"status": "success", "reply_to": msg_json}
            return json.dumps(reply)
