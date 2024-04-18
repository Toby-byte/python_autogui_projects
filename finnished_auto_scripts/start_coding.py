import os
import subprocess
import pyperclip
import pyautogui
import time

# Open a document with the default associated application

# Open fronter
os.startfile('chrome.exe')
time.sleep(4)
pyautogui.hotkey('ctrl', 't')
pyautogui.write("https://kea-fronter.itslearning.com/ContentArea/ContentArea.aspx?LocationID=6460&LocationType=1")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)
pyautogui.press("tab")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)
pyautogui.press("enter")

# Open github
pyautogui.hotkey('ctrl', 't')
pyautogui.write("https://github.com/Toby-byte?tab=repositories")
time.sleep(1)
pyautogui.press("enter")

print("'y' for yes and 'n' for no and 's' for stop")
user_input = input("want me to stop or also generate a web template?: ")

if user_input == "yes" or user_input == "y":
    print("ok, generating a web template...")

    filename = input('What should the file be named?: ')

    base_path = f'C:\\Users\\Tobias Bøge Nielsen\\Desktop\\mapper\\VSCODE_projekter\\{filename}'

    # Create a directory
    os.makedirs(f'{base_path}', exist_ok=True)

    # Paste content from clipboard into a index.html file
    with open(f'{base_path}\\index.html', 'w') as file:
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
        text = pyperclip.paste()
        file.write(str(text))

    # Paste content from clipboard into a style.css file
    with open(f'{base_path}\\style.css', 'w') as file:
        pyperclip.copy("""body { 
    background-color: red; 
};""")
        text = pyperclip.paste()
        file.write(str(text))

    # Paste content from clipboard into a app.js file
    with open(f'{base_path}\\app.js', 'w') as file:
        pyperclip.copy("alert('hello world');")
        text = pyperclip.paste()
        file.write(str(text))

    # Full path to VSCode's executable
    vscode_executable_path = 'D:\\Tobias\\Microsoft VS Code\\Code.exe'

    # Path to the directory you want to open
    directory_path = f'{base_path}'

    # Open the directory in VSCode using the full path to the executable
    subprocess.run([vscode_executable_path, directory_path])

elif user_input == "stop" or user_input == "s" or user_input == "n":
    print("ok, lauching vscode, have a nice day!")
    # Open vscode
    os.startfile("D:/Tobias/Microsoft VS Code/Code.exe")

time.sleep(3)
