import socketserver


class RequestHandler(socketserver.StreamRequestHandler):
    def _dummy_handler(self, data: str) -> str:
        return "got your message mate"

    def handle(self):
        data_bytes: bytes = self.rfile.readline().strip()
        data: str = data_bytes.decode()

        print(f"Recieved message: {data}")
        response: str = self._dummy_handler(data)
        print(f"Response: {response}")

        self.wfile.write((response + "\n").encode())


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), RequestHandler) as server:
        print(f"Server started at {HOST}:{PORT}")
        server.serve_forever()
