"""
Capitalize Words
Write a function capitalize_words that takes a sentence (a string) and returns a new
sentence where the first letter of each word is capitalized.
Example:

Input: capitalize_words("hello world")
Output: "Hello World"
Input: capitalize_words("python is fun")
Output: "Python Is Fun"
"""


def capitalize_words(sentence):
    return sentence.title()


print(capitalize_words("hello world"))
print(capitalize_words("python is fun"))
