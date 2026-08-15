"""Northline freight service. Standard library only -- nothing to install on the box."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from app.consignment import quote
from app.version import deployed_version

PORT = 8080


class Handler(BaseHTTPRequestHandler):
    def _send(self, payload, status=200):
        body = json.dumps(payload, indent=2).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        url = urlparse(self.path)
        if url.path == "/version":
            return self._send(deployed_version())
        if url.path == "/quote":
            q = parse_qs(url.query)
            return self._send(
                quote(
                    q.get("from", ["Kampala"])[0],
                    q.get("to", ["Gulu"])[0],
                    float(q.get("tonnes", ["12"])[0]),
                    float(q.get("km", ["340"])[0]),
                )
            )
        if url.path == "/health":
            return self._send({"status": "ok"})
        self._send({"error": "not found"}, 404)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
