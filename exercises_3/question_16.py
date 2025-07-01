num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

while num > 0:
    remainder = num % 10
    reversed_num = reversed_num * 10 + remainder
    num = num // 10

print(f"{original_num} is palindrome: {original_num == reversed_num}")
