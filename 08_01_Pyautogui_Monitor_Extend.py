# From only my main display(monitor), after pressing the `WIN + p` keys, 
# it will select the `Extend` options to use the monitor`s and the laptop`s display too 

import pyautogui

with pyautogui.hold('win'):
        pyautogui.press(['p'], interval=0.3)

pyautogui.press('p')
pyautogui.press('p')
pyautogui.press('p')
pyautogui.press('enter')