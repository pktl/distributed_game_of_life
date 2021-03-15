import zmq
import json


class Master:
    def __init__(self):
        self.ctx = zmq.Context()
        self.cell_env_req = self.ctx.socket(zmq.REQ)
        self.cell_env_req.connect("tcp://localhost:5555")
        self._ui()

    def _ui(self):
        while inp := input():
            if inp.lower() == "c":
                self.cell_env_req.send_json(json.dumps({
                    "cmd": "create_cell", "args": [(0, 1)]}))
            print(self.cell_env_req.recv_json())
