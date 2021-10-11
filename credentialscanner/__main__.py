import sys
import glob

files = {}

def addFiles(dir: str) -> None:
    global files

    for file in glob.glob(dir + "/*"):
        try:
            with open(dir + "/" + file, "r") as f:
                try:
                    files[dir + "/" + file] = f.read()
                except UnicodeDecodeError:
                    pass
        except IsADirectoryError:
            addFiles(file)

addFiles(".")

foundCredentials = False

for file in files:
    print("Scanning file \'" + file + "\'.")

    lines = files[file].splitlines()

    for line in range(len(lines)):
        for credential in sys.argv[1:]:
            if credential.strip() in lines[line]:
                foundCredentials = True
                print(f"Found credentials in file {file} on line {line + 1}.")
    
    print()

if foundCredentials:
    raise Exception("Credentials were found.")