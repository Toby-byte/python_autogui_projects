import pyautogui
import time
import pyperclip

# X:  159 Y:  213
# click folder
place = pyautogui.locateCenterOnScreen('tests/setup_website_folder.png')
print(place[0], place[1])
pyautogui.moveTo(place[0], place[1], 1)
pyautogui.click()

time.sleep(1)

# new file button
pyautogui.moveTo(200, 80, 1)
pyautogui.click()
pyautogui.write("index.html")
pyautogui.hotkey("enter")

pyperclip.copy("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <script src="app.js" defer></script>
    <title>Document</title>
</head>
<body>
    
</body>
</html>""")
pyautogui.hotkey("ctrl", "v")

# new file button
pyautogui.moveTo(200, 80, 1)
pyautogui.click()
pyautogui.write("style.css")
pyautogui.hotkey("enter")

pyperclip.copy("""body { 
    background-color: red; 
};""")
pyautogui.hotkey("ctrl", "v")

# new file button
pyautogui.moveTo(200, 80, 1)
pyautogui.click()
pyautogui.write("app.js")
pyautogui.hotkey("enter")
pyperclip.copy("alert('hello world');")
pyautogui.hotkey("ctrl", "v")