# Write a Python program to find the common values that appear in two given strings.
def common_values(str1, str2):

    set1 = set(str1)
    set2 = set(str2)
    common_chars = set1.intersection(set2)

    return common_chars


string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
common = common_values(string1, string2)
print("Common characters:", common)
