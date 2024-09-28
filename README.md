---

# Afk-Program

Afk-Program is a cross-platform tool that prevents devices (Windows, Mac, and Linux) from going to sleep or entering idle mode. The program includes an easy-to-use graphical user interface (GUI) for starting and stopping sleep prevention with just a click. This is perfect for ensuring that long-running processes, downloads, or streams aren’t interrupted when you're away from your machine.

## Features
- **Cross-Platform**: Works on Windows, Mac, and Linux.
- **Graphical User Interface (GUI)**: Easily control the sleep prevention with a user-friendly interface.
- **Lightweight**: Minimal system resource usage while keeping your device awake.

## Installation

### Prerequisites
- Python 3.6 or higher installed.
- The following libraries need to be installed:
    ```bash
    pip install tkinter
    ```

### Steps to install:
1. Clone the repository:
    ```bash
    git clone https://github.com/username/Afk-Program.git
    cd Afk-Program
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the program:
    ```bash
    python afk_program.py
    ```

## Usage

### GUI Controls
1. **Start Preventing Sleep**: Click the "Start Preventing Sleep" button to begin keeping the system awake.
2. **Stop Preventing Sleep**: Click the "Stop Preventing Sleep" button to allow the system to sleep again.
3. **Exit**: Click "Exit" to stop sleep prevention and close the application.

### Command Line
- Alternatively, you can run the script directly via the terminal/command line:
    ```bash
    python afk_program.py
    ```

## Platform-Specific Details

### Windows
On Windows, the program uses the `SetThreadExecutionState` function to prevent system sleep.

### MacOS
On macOS, it uses the `caffeinate` command to keep the system awake.

### Linux
On Linux, the program utilizes `systemd-inhibit` to prevent idle mode.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Submit a pull request.

## Contact
For any issues or feature requests, feel free to open an issue or contact the project maintainer at `rijanbhattarailol@example.com`.

---
