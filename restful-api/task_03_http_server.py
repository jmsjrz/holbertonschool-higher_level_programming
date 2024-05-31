#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    A simple HTTP request handler that extends BaseHTTPRequestHandler.
    Handles GET requests for different endpoints and serves JSON data.
    """

    def do_GET(self):
        """
        Handle GET requests.
        """
        if self.path == "/":
            self.send_response(200)  # HTTP status 200 OK
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)  # HTTP status 200 OK
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(response).encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)  # HTTP status 200 OK
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/info":
            self.send_response(200)  # HTTP status 200 OK
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            # HTTP status 404 Not Found
            self.send_error(404, "Endpoint not found")


def run(server_class=HTTPServer,
        handler_class=SimpleHTTPRequestHandler, port=8000):
    """
    Set up and start the HTTP server.

    :param server_class: The HTTP server class to use.
    :param handler_class: The request handler class to use.
    :param port: The port number to bind the server to.
    """
    server_address = ("localhost", port)  # Server address tuple
    # Create server instance
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")  # Log the start of server
    httpd.serve_forever()  # Start the server


if __name__ == "__main__":
    """
    This conditional checks if this script is being run directly.
    If it is, it calls the `run` function to start the server.
    """
    run()  # Run the server if this script is executed directly
