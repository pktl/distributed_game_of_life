import zmq


class Master:
    def __init__(self):
        self.ctx = zmq.Context()
        self.cell_env_req = self.ctx.socket(zmq.REQ)
        self.cell_env_req.connect("tcp://localhost:5555")
        self._ui()

    def _ui(self):
        while inp := input():
            if inp.lower() == "q":
                self.cell_env_req.send_string("q")
                break
            elif inp.lower() == "c":
                self.cell_env_req.send_string("TEST")
            print(self.cell_env_req.recv_string())