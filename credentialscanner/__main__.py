import sys
import glob

files = {}
for file in glob.glob("*"):
    try:
        with open(file, "r") as f:
            try:
                files[file] = f.read()
            except UnicodeDecodeError:
                pass
    except IsADirectoryError:
        pass

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