# By default only my main monitor is used.
# Unfortunately my laptop monitor is lit with black once the system is stood up.
# With this little trick(batch file / one click from TC) I can turn off my laptop`s display.
# It is switching from the 2nd monitor to Extend(to laptop too) and back

import pyautogui

with pyautogui.hold('win'):
        pyautogui.press(['p'], interval=1)

pyautogui.press('p')
pyautogui.press('p')
pyautogui.press('p')
pyautogui.press(['enter'], interval=0.5)
pyautogui.press('p')
pyautogui.press('enter')