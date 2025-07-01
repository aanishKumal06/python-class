"""
Reverse Words in Sentence (Strings and Loops)
Write a function reverse_words(sentence) that takes a sentence and reverses the order of
characters in each word while keeping the word order intact. For example,
reverse_words("Hello World") returns "olleH dlroW". Use string methods like split()
and join() and a loop to reverse each word.
"""


def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return ' '.join(reversed_words)


print(reverse_words("Hello World"))
