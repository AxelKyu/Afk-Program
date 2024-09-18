import pyautogui as pag
import time
import random

# Pointing the mouse at a different direction
while True:
    x = random.randint(400, 800)
    y = random.randint(400, 800)
    pag.moveTo(x, y, 1.0)
    time.sleep(2)

