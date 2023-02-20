import pyautogui
import random
import time

i = 0

while True:
    # Generate random coordinates within the screen bounds
    x, y = random.randint(0, pyautogui.size()[0]), random.randint(0, pyautogui.ize()[1])

    # Move the mouse cursor to the random coordinates smoothly
    duration = random.uniform(0.5, 1.5)  # random duration between 0.5 and 1.5 seconds
    pyautogui.moveTo(x, y, duration=duration)

    # Wait for 1 second
    time.sleep(1)