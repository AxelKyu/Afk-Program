import platform
import time
import subprocess
import os
import tkinter as tk
from tkinter import messagebox

# Function to prevent system sleep
def prevent_sleep():
    current_os = platform.system()

    if current_os == "Windows":
        import ctypes
        # Windows: Prevent system sleep
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
    elif current_os == "Linux":
        # Linux: Use systemd-inhibit to prevent system sleep
        return subprocess.Popen(['systemd-inhibit', '--what=idle', '--why="Prevent system from sleeping"', '--mode=block', 'sleep', '999999'])
    elif current_os == "Darwin":
        # macOS: Use caffeinate to prevent system sleep
        return subprocess.Popen(['caffeinate', '-dims'])
    else:
        raise NotImplementedError(f"Unsupported OS: {current_os}")

# Function to allow system sleep again
def allow_sleep(inhibit_process=None):
    current_os = platform.system()

    if current_os == "Windows":
        import ctypes
        # Windows: Allow system sleep
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
    elif current_os in ["Linux", "Darwin"] and inhibit_process:
        # Linux/macOS: Kill the sleep-inhibiting process
        inhibit_process.terminate()

# Function to handle the start button
def start_preventing_sleep():
    global inhibit_process
    if inhibit_process is None:
        inhibit_process = prevent_sleep()
        status_label.config(text="Sleep prevention: ON", fg="green")
    else:
        messagebox.showinfo("Info", "Sleep prevention is already active!")

# Function to handle the stop button
def stop_preventing_sleep():
    global inhibit_process
    if inhibit_process is not None:
        allow_sleep(inhibit_process)
        inhibit_process = None
        status_label.config(text="Sleep prevention: OFF", fg="red")
    else:
        messagebox.showinfo("Info", "Sleep prevention is not active!")

# Function to close the GUI and exit the program
def on_exit():
    if inhibit_process:
        allow_sleep(inhibit_process)
    root.quit()

# GUI Setup
root = tk.Tk()
root.title("Sleep Prevention Tool")
root.geometry("300x200")

# Status label to show sleep prevention state
status_label = tk.Label(root, text="Sleep prevention: OFF", fg="red", font=("Arial", 12))
status_label.pack(pady=20)

# Start button
start_button = tk.Button(root, text="Start Preventing Sleep", command=start_preventing_sleep, font=("Arial", 10), width=25)
start_button.pack(pady=10)

# Stop button
stop_button = tk.Button(root, text="Stop Preventing Sleep", command=stop_preventing_sleep, font=("Arial", 10), width=25)
stop_button.pack(pady=10)

# Exit button
exit_button = tk.Button(root, text="Exit", command=on_exit, font=("Arial", 10), width=25)
exit_button.pack(pady=10)

# Global variable to hold the sleep prevention process (if applicable)
inhibit_process = None

# Handle exit event
root.protocol("WM_DELETE_WINDOW", on_exit)

# Start the GUI event loop
root.mainloop()
