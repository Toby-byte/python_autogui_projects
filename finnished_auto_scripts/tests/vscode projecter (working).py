import os 
import pyperclip
import subprocess

base_path = 'C:\\Users\\Tobias Bøge Nielsen\\Desktop\\mapper\\VSCODE_projekter\\'

# Create a directory
os.makedirs(f'{base_path}new_project', exist_ok=True)

# Paste content from clipboard into a index.html file
with open(f'{base_path}\\new_project\\index.html', 'w') as file:
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
with open(f'{base_path}\\new_project\\style.css', 'w') as file:
    pyperclip.copy("""body { 
    background-color: red; 
};""")
    text = pyperclip.paste()
    file.write(str(text))

# Paste content from clipboard into a app.js file
with open(f'{base_path}\\new_project\\app.js', 'w') as file:
    pyperclip.copy("alert('hello world');")
    text = pyperclip.paste()
    file.write(str(text))

# Full path to VSCode's executable
vscode_executable_path = 'D:\\Tobias\\Microsoft VS Code\\Code.exe'

# Path to the directory you want to open
directory_path = f'{base_path}\\new_project'

# Open the directory in VSCode using the full path to the executable
subprocess.run([vscode_executable_path, directory_path])