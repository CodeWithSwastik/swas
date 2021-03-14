import json
import os
import subprocess
import uuid
from http.server import BaseHTTPRequestHandler
from urllib import parse


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        code_params = parse.parse_qs(parse.urlparse(self.path).query).get("code")
        if not code_params or not code_params[0]:
            self.send_response(400)
            self.set_headers()
            return self.wfile.write(
                json.dumps({"error_message": "Missing field code"}).encode()
            )
        code = code_params[0]

        tmpfile = "/tmp/" + str(uuid.uuid1())[:12] + ".swas"
        with open(tmpfile, "w") as f:
            f.write(code)

        process = subprocess.Popen(
            ["python", "-m", "swas", tmpfile],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = process.communicate()

        data = {"stdout": stdout.decode(), "stderr": stderr.decode()}

        self.send_response(200)
        self.set_headers()
        self.wfile.write(json.dumps(data).encode())

        os.remove(tmpfile)

    def set_headers(self):
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
