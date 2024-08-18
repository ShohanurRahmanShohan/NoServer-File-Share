# NoServer File Share

**NoServer File Share** is a lightweight and user-friendly file sharing application that requires no server setup, provides instant file sharing without upload time, and supports fast transfer speeds. Ideal for sharing files quickly and efficiently, this application is designed with simplicity and performance in mind.

## Download

[![Download](https://img.icons8.com/ios-filled/50/000000/download.png)](https://github.com/ShohanurRahmanShohan/NoServer-File-Share/releases/download/exe/NoServerShare.exe)
- **Direct Download**: [file_server.exe](https://github.com/ShohanurRahmanShohan/NoServer-File-Share/releases/download/exe/NoServerShare.exe)

## Features

- **No Server Required**: Run the application on your local machine without the need for any external server setup.
- **Instant File Sharing**: Share files immediately without waiting for upload times.
- **No Restrictions**: Share any type of file without limitations on file size or type.
- **BDIX Speed**: Utilizes high-speed local network transfer (BDIX) for fast file sharing.
- **User-Friendly Interface**: Simple and intuitive interface built with PyQt5.
- **Responsive UI**: Access your files through a responsive web interface served by Flask.
- **Stop Server Functionality**: Easily stop the server with a single button.
- **Status Indicator**: Get real-time status updates with a clickable link to the server URL.
- **Customizable**: Includes a cute icon and customizable footer with a link to the creator’s profile.

## Installation (Windows)

1. **Download the Executable**:
   - You can download the latest version of the application directly from the [releases page](https://github.com/ShohanurRahmanShohan/NoServer-File-Share/releases).
   - Alternatively, download it directly here: [file_server.exe](https://github.com/ShohanurRahmanShohan/NoServer-File-Share/releases/download/exe/file_server.exe).

2. **Run the Application**:
   - Double-click the `file_server.exe` file to start the application.

3. **Port Forwarding**:
   - To expose your local server to the internet, you can use Serveo with the following command in CMD:
     ```bash
     ssh -R 80: your_link serveo.net
     ```

## Installation (Linux)

1. **Clone the Repository**:
   - Open your terminal and run:
     ```bash
     git clone https://github.com/ShohanurRahmanShohan/NoServer-File-Share.git
     cd NoServer-File-Share
     ```

2. **Run the Application**:
   - You can use the following bash script to set up and run the application:

     ```bash
     #!/bin/bash

     # Define variables
     PROJECT_DIR="NoServer-File-Share"
     REPO_URL="https://github.com/ShohanurRahmanShohan/NoServer-File-Share.git"
     VENV_DIR="venv"
     FLASK_SCRIPT="flask_app.py"

     # Clone the GitHub repository
     git clone $REPO_URL
     cd $PROJECT_DIR

     # Create a new virtual environment
     python3 -m venv $VENV_DIR

     # Activate the virtual environment
     source $VENV_DIR/bin/activate

     # Install the required Python packages
     pip install -r requirements.txt

     # Run the Flask application script
     python $FLASK_SCRIPT &

     # Start port forwarding with Serveo
     ssh -R 80:localhost:1234 serveo.net
     ```
 **Access the Application**:
   - Once the server is running, you can access it by visiting `http://localhost:1234` or the public URL provided by Serveo.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
