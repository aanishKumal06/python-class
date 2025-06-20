x = 5               # int
pi = 3.14           # float
z = 2 + 3j          # complex
name = "Anish"      # str
colors = ["red", "blue"]  # list
point = (4, 5)      # tuple
student = {"name": "Ram", "age": 20}  # dict
fruits = {"apple", "banana"}  # set
is_active = True    # bool
data = b"binary"    # bytes


snacks = ["roti", "biscuits", "Chips", "noodles", ["Ram", "Shyam"]]
print(snacks[4][1])

personal_details = {
    "name": "Ram Sharma",
    "address": "Pokhara"
}


print(personal_details['address'])

data = [
    {
     "name": "Ram Sharma",
     "hobbies": ["coding", {
         'hi': {
             'hello': [{
                 'tree': ["root", {
                     'complex': [True]
                 }]
             }]
         }
     }]
    }
]


print(data[0]["hobbies"][1]["hi"]["hello"][0]['tree'][1]['complex'][0])
