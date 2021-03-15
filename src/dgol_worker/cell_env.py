import zmq
import json
from typing import Union
from ..dgol_worker.cell import Cell
from ..dgol_support import CellState, Position


class CellEnv:
    def __init__(self):
        self.positions = set()
        # Map positions to Cell objects
        self.cells = dict()
        self.cmd_server = CmdServer()

    def __repr__(self):
        return "\n".join([repr(c) for c in self.cells])

    def create_cell(self,
                    position: Position,
                    state: Union[CellState, str] = CellState.DEAD):
        if position not in self.positions:
            self.positions.add(position)
            self.cells[position] = Cell(position, state)

    def delete_cell(self, position: Position):
        if position in self.positions:
            self.positions.remove(position)
            del self.cells[position]


class CmdServer:
    def __init__(self, port: int = 5555):
        self.ctx = zmq.Context()
        self.rep = self.ctx.socket(zmq.REP)
        self.rep.bind(f"tcp://*:{port}")
        #self._server_loop(self.rep)

    def _server_loop(self):
        while True:
            msg = self.rep.recv_json()
            self.rep.send_json(self._reply_to(msg))

    def _reply_to(self, msg_json):
        msg_dict = json.loads(msg_json)
        if msg_dict["cmd"] == "create_cell":
            self.create_cell(msg_dict["args"][0])
            reply = {"status": "success", "reply_to": msg_json}
            return json.dumps(reply)
