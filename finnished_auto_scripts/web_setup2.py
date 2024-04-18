import pyperclip # Good for avoiding formatting issues
import os

# Create a directory
os.makedirs('new_project', exist_ok=True)

# Paste content from clipboard into a index.html file
with open('new_project/index.html', 'w') as file:
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
with open('new_project/style.css', 'w') as file:
    pyperclip.copy("""body { 
    background-color: red; 
};""")
    text = pyperclip.paste()
    file.write(str(text))

# Paste content from clipboard into a app.js file
with open('new_project/app.js', 'w') as file:
    pyperclip.copy("alert('hello world');")
    text = pyperclip.paste()
    file.write(str(text))