from collections import Counter

lines = input("Enter Lines for the count frequency: ")
print(Counter(lines.split()))

words = lines.split(" ")

counter_dict = {}

for word in words:
    if word in counter_dict:
        counter_dict[word] += 1
    else:
        counter_dict[word] = 1


print(counter_dict)
