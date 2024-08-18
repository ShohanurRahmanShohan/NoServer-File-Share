import os
import socket
import threading
from flask import Flask, send_from_directory, render_template_string
import logging
from rich.console import Console
from rich.prompt import Prompt

# Suppress Flask's default logging completely
log = logging.getLogger('werkzeug')
log.disabled = True
flask_app = Flask(__name__)
flask_app.logger.disabled = True

# Initialize other variables
selected_path = ""
server_running = True
server_url = "http://localhost:1234"

# HTML template for the file server
index_html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Server</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { padding: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Files in Directory</h1>
        <ul class="list-group">
            {% for filename in files %}
                <li class="list-group-item">
                    <a href="{{ url_for('serve_file', filename=filename) }}">{{ filename }}</a>
                </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
'''

@flask_app.route('/')
def index():
    files = os.listdir(selected_path)
    return render_template_string(index_html_template, files=files)

@flask_app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(selected_path, filename)

def start_flask_app():
    global server_running
    # Flask app will now run silently
    flask_app.run(host='0.0.0.0', port=1234, use_reloader=False, debug=False)
    server_running = False

def stop_flask_server():
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

def select_directory(console):
    global selected_path, server_url
    selected_path = Prompt.ask("[bold yellow]Enter the path of the directory to share[/]", default="/")
    
    while not os.path.isdir(selected_path):
        selected_path = Prompt.ask("[bold red]Invalid path![/] Please enter a valid directory path")

    local_ip = get_local_ip()
    server_url = f"http://{local_ip}:1234"
    console.print(f"\n[bold green]Selected path:[/] {selected_path}")
    console.print(f"[bold cyan]Server is running at:[/] {server_url}\n")
    start_flask_server()

def start_flask_server():
    server_thread = threading.Thread(target=start_flask_app)
    server_thread.daemon = True
    server_thread.start()

def main():
    console = Console()
    console.print("[bold magenta]NoServer File Share[/]", justify="center", style="bold")
    console.print("🌀 [bold blue]Starting file server...[/] 🌀", justify="center")
    select_directory(console)

    try:
        while server_running:
            pass  # Keep the server running
    except KeyboardInterrupt:
        stop_flask_server()
        console.print("[bold red]Server stopped.[/]")

if __name__ == "__main__":
    main()
