# It is switching from the 2nd monitor to Extend(laptop screen too) and back

import pyautogui

with pyautogui.hold('win'):
        pyautogui.press(['p'], interval=1)

pyautogui.press('p')
pyautogui.press('p')
pyautogui.press('p')
pyautogui.press(['enter'], interval=0.5)
pyautogui.press('p')
pyautogui.press('enter')