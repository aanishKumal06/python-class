# Write a Python program to access only unique key value of a Python object.

import json

python_obj = '{"Ram":  45, "Ram":  12, "Ram":  33, "Hema": 41, "Hema": 41, "Hema": 22}'
print("Original Python object:")
print(python_obj)

json_obj = json.loads(python_obj)
print("\nUnique Key in a JSON object:")
print(json_obj)
