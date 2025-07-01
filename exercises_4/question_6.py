"""
Longest Word Finder (Strings and Loops)
Write a function longest_word(sentence) that takes a sentence and returns the longest
word. If multiple words have the same maximum length, return the first one. Use string
methods like split() and a loop. For example, longest_word("I love programming")
returns "programming".
"""


def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


print(longest_word("I love programming"))
