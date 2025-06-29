# Write a Python program to convert JSON data to Python object.

import json

personal_details = '{"name": "Hema", "age": 25, "city": "KTM"}'

python_obj = json.loads(personal_details)

print("Python object:", python_obj)
print("Type:", type(python_obj))
