import pyautogui
import time

# Open Notepad
pyautogui.hotkey('win', 'r')
time.sleep(0.5)
pyautogui.typewrite('notepad', interval=0.1)
pyautogui.press('enter')
time.sleep(2)

# Type some text
pyautogui.typewrite('Hello, PyAutoGUI!\n', interval=0.1)
time.sleep(1)

# Save the file
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.typewrite('example.txt', interval=0.1)
pyautogui.press('enter')