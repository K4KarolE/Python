# pyautogui installation: Win: py -m pip install pyautogui \\ Linux: python3 -m pip install pyautogui \\ https://pyautogui.readthedocs.io/en/latest/install.html
# From my main display(monitor), after pressing the `WIN key + p` keys it will select the 'Extend' options to use the monitor's and the laptop's display too
# Linux Mint: no `WIN key + p` menu -> it switches between the different display sharing options every time the `WIN key + p` combination is actioned

import pyautogui

with pyautogui.hold('win'):
        pyautogui.press(['p'], interval=0.3)

pyautogui.press(['p'], interval=0.2)
pyautogui.press(['p'], interval=0.2)
pyautogui.press(['p'], interval=0.2)
pyautogui.press('enter')


