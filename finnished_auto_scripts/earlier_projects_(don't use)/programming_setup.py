import pyautogui
import time
import pyperclip

name_of_folder = input("Enter foldername: ")


pyautogui.moveTo(200, 80, 1)
pyautogui.click()

time.sleep(1)

pyperclip.copy(name_of_folder)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
