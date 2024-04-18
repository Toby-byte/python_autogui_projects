import pyautogui
import time
import os

try:
    # by using an image we can navigte 
    # to place on the screen where the CENTER of image is located
    website_folder = 'tests/setup_website_folder.png'
    new_file = 'tests/new_file.png'

    if os.path.exists(website_folder) and os.path.exists(website_folder):
        pyautogui.locateCenterOnScreen(website_folder, confidence=0.9)
        new_file = pyautogui.locateCenterOnScreen(new_file, confidence=0.9)

        time.sleep(1)

        # this prints out the coordinates 
        print(website_folder[0], website_folder[1])

        time.sleep(1)

        # this moves the mouse there with the duration of 1 second
        pyautogui.moveTo(website_folder[0], website_folder[1], 1)
        pyautogui.rightClick()
        pyautogui.moveTo(new_file[0], new_file[1], 1)
    else:
        print('folders not found')
except Exception as ex:
    print(ex)


