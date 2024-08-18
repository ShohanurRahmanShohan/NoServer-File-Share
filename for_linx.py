import os
import socket
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from pathlib import Path

# Initialize other variables
selected_path = ""
server_running = True
server_url = "http://localhost:1234"

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Construct the full path to serve files
        path = super().translate_path(path)
        if path.startswith(selected_path):
            return path
        return os.path.join(selected_path, path.lstrip('/'))

def start_http_server():
    global server_running
    server_address = ('0.0.0.0', 1234)
    httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
    print(f"Serving at {server_url}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        server_running = False
        httpd.server_close()

def stop_server():
    global server_running
    server_running = False

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        s.connect(('10.254.254.254', 1))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        s.close()
    return local_ip

def select_directory():
    global selected_path, server_url
    selected_path = input("Enter the path of the directory to share: ")
    
    while not Path(selected_path).is_dir():
        selected_path = input("Invalid path! Please enter a valid directory path: ")

    local_ip = get_local_ip()
    global server_url
    server_url = f"http://{local_ip}:1234"
    print(f"\nSelected path: {selected_path}")
    print(f"Server is running at: {server_url}\n")
    start_http_server()

def main():
    print("NoServer File Share")
    print("🌀 Starting file server... 🌀")
    select_directory()

    try:
        while server_running:
            pass  # Keep the server running
    except KeyboardInterrupt:
        stop_server()
        print("Server stopped.")

if __name__ == "__main__":
    main()
