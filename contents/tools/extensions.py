import os
import json
import subprocess




file =  os.path.abspath(__file__)
file_extensions   = os.path.join(os.path.dirname(file), "../../.vscode/extensions.json")




command = "code --list-extensions"

extensions = subprocess.run(
    command,
    shell=True,
    check=True,
    stdout=subprocess.PIPE,
    text=True
).stdout.splitlines()

content = {
    "recommendations": extensions
}


with open(file_extensions, "w") as json_file:
    json.dump(content, json_file, indent=4)
