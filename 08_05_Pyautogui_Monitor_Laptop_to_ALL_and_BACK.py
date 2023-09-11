# Laptop --> Laptop + Additional Screen
# Laptop + Additional Screen --> Laptop

import pyautogui

with pyautogui.hold('win'):
        pyautogui.press(['p'], interval=0.3)

pyautogui.press(['p'], interval=0.2)
pyautogui.press(['p'], interval=0.2)
pyautogui.press('enter')


