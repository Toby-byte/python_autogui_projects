import pyautogui
import time

for i in range(3):

    time.sleep(1)

    # new file button
    pyautogui.moveTo(144, 80, 2)
    pyautogui.click()
    pyautogui.write(f"hello_world{i}.py")
    pyautogui.hotkey("enter")

    time.sleep(1)

    # X:  662 Y:  205
    pyautogui.moveTo(662, 205, 2)
    pyautogui.click()
    pyautogui.write("import time")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.write("print('Hello World')")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.write("time.sleep(5)")

    time.sleep(1)

    # coordinates of terminal button
    pyautogui.moveTo(1716, 20, 2)
    pyautogui.click()
    pyautogui.click()
    pyautogui.write(f".\hello_world{i}.py")
    pyautogui.press("enter")