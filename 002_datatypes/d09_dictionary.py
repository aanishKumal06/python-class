# from pprint import pprint

basic_info = {
    "name": "Ram",
    "Age": 19
}
b = basic_info.copy()

extra_info = {
    "nickname": "Ramu",
    "name": "Shyam"
}
e = extra_info.copy()

# basic_info.update(extra_info)
# short hand of update in dictionary
basic_info = basic_info | extra_info
print(basic_info)
