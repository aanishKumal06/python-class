import json

file_path = r"C:\Users\anish\OneDrive\Desktop\python-class\.vscode\extensions.json"

with open(file_path, "r") as fp:
    content = json.load(fp)
    print(content["recommendations"][0])
