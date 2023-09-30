# Speaker --> Headset
# OS: Win 11
# Output Devices: 2


import pyautogui

with pyautogui.hold('win'):
        with pyautogui.hold('ctrl'):
            pyautogui.press(['v'], interval=1)
pyautogui.press(['down'], interval=0.5)
pyautogui.press(['enter'])

