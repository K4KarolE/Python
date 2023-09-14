# Switching the Sound`s state between MUTED and UNMUTED
# Screen: 2560 x 1440
# Scale: 150% (laptop)
# OS: Win 11

import pyautogui

# Sound Icon
pyautogui.leftClick(2430, 1410, interval=0.5)

# Sound Mute / Unmute
pyautogui.leftClick(2060, 1220)

# Click Away
pyautogui.leftClick(2560/2, 1440/2)