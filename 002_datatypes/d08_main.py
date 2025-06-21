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
