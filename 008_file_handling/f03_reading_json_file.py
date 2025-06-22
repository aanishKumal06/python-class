import json

file_path = r"C:\Users\anish\OneDrive\Desktop\python-class\.vscode\extensions.json"

with open(file_path, "r") as fp:
    content = json.load(fp)
    print(content["recommendations"][0])


personal_details = '{"name": "Anish", "age": 18, "city": "Pokhara"}'

convert_to_dist = json.loads(personal_details)


for key, value in convert_to_dist.items():
    print("Key: ", key, "Value: ", value)
