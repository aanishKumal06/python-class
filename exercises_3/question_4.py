"""
Vowel Counter
Write a function count_vowels that takes a string and returns the number of vowels
(a, e, i, o, u, both lowercase and uppercase) in it.
Example:

Input: count_vowels("Hello World")
Output: 3
Input: count_vowels("PYTHON")
Output: 1
"""


def count_vowels(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    user_vowel_letters = []
    for char in word:
        if char in vowels:
            user_vowel_letters.append(char)
    print("Vowels found:", user_vowel_letters)
    print("Total vowels:", len(user_vowel_letters))


user_input = input("Enter a string: ")
count_vowels(user_input)
