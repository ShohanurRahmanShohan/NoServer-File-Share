import sys
import os
import socket
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from PyQt5.QtGui import QIcon
from flask import Flask, send_from_directory, render_template_string

flask_app = Flask(__name__)
selected_path = ""
server_running = True
server_url = "http://localhost:1234"

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
    flask_app.run(host='0.0.0.0', port=1234, use_reloader=False)
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

# PyQt5 UI setup
class FileServerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.info_label = QLabel("Select a folder to host:")
        self.layout.addWidget(self.info_label)

        self.select_button = QPushButton('Select Folder')
        self.select_button.clicked.connect(self.showDialog)
        self.layout.addWidget(self.select_button)

        self.stop_button = QPushButton('Stop Server')
        self.stop_button.clicked.connect(self.stopServer)
        self.layout.addWidget(self.stop_button)

        self.status_label = QLabel('<a href="#" style="text-decoration: none; color: red;">Server Status: Not Running</a>')
        self.status_label.setOpenExternalLinks(True)
        self.layout.addWidget(self.status_label)
        self.footer = QLabel(
            '<a href="https://www.facebook.com/0Shohan0/" style="text-decoration: none; color: black;">Made with love by <a href="https://www.facebook.com/0Shohan0/" style="color: black;">Shohan</a></a>'
        )
        self.footer.setOpenExternalLinks(True)
        self.footer.setStyleSheet("font-size: 12px;")
        self.layout.addWidget(self.footer)

        self.setLayout(self.layout)
        self.setWindowTitle('NoServer File Share') 
        self.setGeometry(100, 100, 300, 200)
        self.setWindowIcon(QIcon('path/to/your/cute_icon.ico'))  
        self.show()

    def showDialog(self):
        global selected_path, server_url
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        selected_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        
        if selected_path:
            local_ip = get_local_ip()
            server_url = f"http://{local_ip}:1234"
            self.info_label.setText(f"Selected path: {selected_path}")
            self.status_label.setText(f'<a href="{server_url}" style="text-decoration: none; color: green;">Server Status: Running at {server_url}</a>')
            self.status_label.setOpenExternalLinks(True)
            self.startFlaskServer()

    def startFlaskServer(self):
        server_thread = threading.Thread(target=start_flask_app)
        server_thread.daemon = True
        server_thread.start()

    def stopServer(self):
        stop_flask_server()
        self.status_label.setText('<a href="#" style="text-decoration: none; color: red;">Server Status: Not Running</a>')
        self.status_label.setOpenExternalLinks(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileServerUI()
    sys.exit(app.exec_())
