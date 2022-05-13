import socketserver
import typing as tp

from db import Database

db = Database()


def is_passcode_valid(passcode: str) -> bool:
    return len(passcode) == 4 and passcode.isnumeric()


class RequestHandler(socketserver.StreamRequestHandler):
    def _ping(self, args: tp.List[str]) -> str:
        if len(args) != 0:
            print(f"Warning, expected no args, got {args}")
        return "PONG " + " ".join(args)

    def handle(self):
        data_bytes: bytes = self.rfile.readline().strip()
        data: str = data_bytes.decode(encoding="utf-8")
        command, *args = data.split()
        print(f"Recieved command: '{command}' with args {args}")

        if command == "PING":
            response = self._ping(args)
        else:
            ...
            # MORE HANDLERS

        print(f"Response: '{response}'")
        self.wfile.write((response + "\n").encode(encoding="utf-8"))


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), RequestHandler) as server:
        print(f"Server started at {HOST}:{PORT}")
        server.serve_forever()
