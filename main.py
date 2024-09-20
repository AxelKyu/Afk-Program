import pyautogui as pag
import time
import random
import keyboard

# Pointing the mouse at a different direction
while True:
    time.sleep(1)
    if keyboard.is_pressed("0"):
        break
    else:
        x = random.randint(400, 800)
        y = random.randint(400, 800)
        pag.moveTo(x, y, 1.0)


