import pyautogui as pag
import time
import random
import keyboard

# Pointing the mouse at a different direction
while True:
    if keyboard.read_key() == "0":
        break
    else:
        x = random.randint(400, 800)
        y = random.randint(400, 800)
        pag.moveTo(x, y, 1.0)
        time.sleep(2)


