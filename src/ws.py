"""
Super Simple HTTP Server in Python .. not for production just for learning and fun
Author: Wolf Paulus (https://wolfpaulus.com)
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import asctime
from main import is_odd
from json import dumps

hostName = "0.0.0.0"
serverPort = 8080
template = '<li>{name} : <a href="{server}" target="_blank">{project}</a> | <a href="{github}" target="_blank">Github</a> | <a href="{docker}" target="_blank">Container Image</a></li>'


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        status, content, content_type = 404, "Not Found", "text/html"  # setting default values
        if self.path == "/health":
            status, content, content_type = 200, "OK", "text/html"
        elif self.path == "/":
            with open('./src/students.json', 'r') as f:
                li = "\n".join([template.format(**s) for s in json.load(f)])
            with open('./src/index.html', 'r') as f:
                status, content, content_type = 200, f.read().format(li=li), "text/html"
        elif self.path.startswith("/?number="):
            number = self.path.split("=")[1] if self.path.startswith("/?number=") else ""
            result = f"{number} is {'odd' if is_odd(int(number)) else 'even'}." if number.isnumeric() else ""
            if self.headers.get('Accept') == 'application/json':
               pass
            else:
                with open('./src/response.html', 'r') as f:
                    # read the html template and fill in the parameters: path, time and result
                    status, content = 200, f.read().format(path=self.path, time=asctime(), result=result)
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.end_headers()
        self.wfile.write(bytes(content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
