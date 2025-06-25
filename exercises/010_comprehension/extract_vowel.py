# Extract all vowels from a string using list comprehension.

name = input("Enter Your Name: ")

VOWElS_LETTER = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

user_vowel_letter = [char for char in name if char in VOWElS_LETTER]

print(user_vowel_letter)
