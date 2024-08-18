# NoServer File Share

**NoServer File Share** is a lightweight and user-friendly file sharing application that requires no server setup, provides instant file sharing without upload time, and supports fast transfer speeds. Ideal for sharing files quickly and efficiently, this application is designed with simplicity and performance in mind.

## Download

[![Download](https://img.icons8.com/color/50/000000/download.png)](https://github.com/ShohanurRahmanShohan/NoServer-File-Share/releases/download/exe/NoServerShare.exe)
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

To run the application on Linux, Use this bash script:

```bash
#!/bin/bash

# Define variables
REPO_URL="https://raw.githubusercontent.com/ShohanurRahmanShohan/NoServer-File-Share/main/for_linx.py"
SCRIPT_NAME="for_linx.py"
VENV_DIR="venv"

# Download the Python script
curl -o "$SCRIPT_NAME" "$REPO_URL"

# Check if the download was successful
if [ $? -eq 0 ]; then
    echo -e "\n${SCRIPT_NAME} has been successfully downloaded."
    echo -e "To run the script, use: \n  python $SCRIPT_NAME\n"
else
    echo -e "\nFailed to download ${SCRIPT_NAME}. Please check the URL and try again.\n"
fi


```
**Port Forwarding**:
   - To expose your local server to the internet :
     ```bash
     ssh -R 80:localhost:1234 serveo.net
     ```
## Created By

**Shohanur Rahman** - Part-time coder, full-time engineering student. Just a curious mind trying to make things easier for everyone! 🚀😄

*Fun Fact*: Did you know that the longest file name allowed on Windows is 260 characters? That's quite a lot of room for creative naming!
