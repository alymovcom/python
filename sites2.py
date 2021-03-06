import sys
import os

try:
    site_name = sys.argv[1]
    try:
        folder = sys.argv[2]
    except IndexError:
        folder = "sites"
    
    folder = "/Users/igor_alymov/Documents/" + folder + "/" + site_name
    os.mkdir(folder)
    with open(folder + "/index.html", "w") as file:
        file.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
</head>
<body>
    
    <script src="script.js"></script>
</body>
</html>""")

    with open(folder + "/style.css", "w"):
        pass
    with open(folder + "/script.js", "w"):
        pass
    os.mkdir(folder + "/imgs")

except IndexError:
    print("error-91")
