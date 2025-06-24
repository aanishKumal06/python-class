"""Write a Python program that takes a list of Nepali comedy character names (written in English letters) 
and groups them in a dictionary based on the first letter of each name. """

names = [
    "Mundre", "Magne Buda", "Jire Khursani", "Mundre Junior", "Gaida", "Magne",
    "Chankhe", "Dhurmus", "Suntali", "Pooja Sharma", "Junu", "Bale",
    "Chankhe Junior", "Phool Baje", "Takme Buda", "Kale Dai", "B.K.",
    "Sakal", "Dhurmus Junior", "Rajaram", "Thakur", "Suntali Junior"
]
groups = {}

for name in names:
    first_letter = name[0]
    if first_letter not in groups:
        groups[first_letter] = []
    groups[first_letter].append(name)

print(groups)
