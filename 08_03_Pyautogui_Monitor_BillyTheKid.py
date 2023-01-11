# It will randomly select a number from the range -> that many times makes the display sharing (1 or 2 display, if only 1: monitor or paptop)
# selector jump and eventually selecting the option in the latest loop

import pyautogui
import random

x_times = random.randrange(1,20)

print(x_times)

with pyautogui.hold('win'):
        pyautogui.press(['p'], interval=0.3)

z = 0  #counter

while z != x_times:
        pyautogui.press('p', interval=0.3)
        z += 1
else:
        pyautogui.press('enter')