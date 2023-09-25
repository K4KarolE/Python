# After pressing the `WIN + p` keys, from the `Extend` option (Extend = using the monitor`s and the laptop`s display the same time)
# it will jump to the `Second screen only` which is my main display/monitor 

import pyautogui

with pyautogui.hold('win'):
        pyautogui.press(['p'], interval=0.3)

pyautogui.press('p')
pyautogui.press('enter')