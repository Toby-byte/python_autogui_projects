import pyautogui
import time
import pyperclip

with pyautogui.hold('ctrl'):
    pyautogui.press(['j'])

time.sleep(1)

with pyautogui.hold('ctrl'):
    pyautogui.press(['j'])

time.sleep(1)

# new file button
pyautogui.moveTo(144, 80, 2)
pyautogui.click()
pyautogui.write("hello_world.py")
pyautogui.hotkey("enter")

time.sleep(1)

pyperclip.copy("@")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.write("hello")
