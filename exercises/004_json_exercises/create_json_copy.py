# Write a Python program to create a new JSON file from an existing JSON file.

import json

existing_file = 'existing.json'
new_file = 'new_file.json'

with open(existing_file, 'r') as file:
    data = json.load(file)

with open(new_file, 'w') as fp:
    json.dump(data, fp)

print(f"Copied data from {existing_file} to {new_file} successfully.")
