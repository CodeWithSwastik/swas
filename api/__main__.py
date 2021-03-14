from http.server import HTTPServer

from .run import handler


def main():
    server = HTTPServer(("localhost", 8080), handler)
    print("Starting server, use <Ctrl-C> to stop")
    server.serve_forever()


if __name__ == "__main__":
    main()
