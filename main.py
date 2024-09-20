import ctypes
import pyautogui as pag
import time
import random
import keyboard

# Prevent the system from going to sleep
ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

try:
    # Pointing the mouse at a different direction
    while True:
        time.sleep(1)
        if keyboard.is_pressed("0"):
            break
        else:
            x = random.randint(400, 800)
            y = random.randint(400, 800)
            pag.moveTo(x, y, 1.0)
finally:
    # Allow the system to sleep again after the program ends
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
