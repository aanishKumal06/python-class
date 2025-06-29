name = input("Enter your name: ")
VOWEL_LETTERS = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
user_vowel_letters = []

for char in name:
    if char in VOWEL_LETTERS:  # Membership checker
        user_vowel_letters.append(char)

print(user_vowel_letters)
