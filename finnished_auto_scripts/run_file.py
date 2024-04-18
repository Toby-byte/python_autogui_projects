import os
import pyperclip
import pyautogui
import time

# Open a document with the default associated application

# Open fronter
os.startfile('chrome.exe')
time.sleep(2)
pyautogui.hotkey('ctrl', 't')
pyautogui.write("https://kea-fronter.itslearning.com/ContentArea/ContentArea.aspx?LocationID=6460&LocationType=1")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("tab")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("enter")

# Open github
pyautogui.hotkey('ctrl', 't')
pyautogui.write("https://github.com/Toby-byte?tab=repositories")
time.sleep(1)
pyautogui.press("enter")

# Open vscode
os.startfile("D:/Tobias/Microsoft VS Code/Code.exe")

