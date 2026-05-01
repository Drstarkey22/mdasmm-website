#!/usr/bin/env python3
"""
Simple HTTP server for SMM website.
Usage: python3 serve.py [port]
Default port: 4200
"""
import http.server
import socketserver
import sys
import os

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4200
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        print(f"[SMM] {self.address_string()} - {format % args}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"╔══════════════════════════════════════════════╗")
    print(f"║  Strategic Medical Management — Web Server   ║")
    print(f"║  http://localhost:{PORT:<29s}║")
    print(f"╚══════════════════════════════════════════════╝")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
