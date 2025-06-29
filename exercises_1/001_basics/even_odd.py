numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_odd_dict = {}
for num in numbers:
    if num % 2 == 0:
        even_odd_dict[num] = "Even"
    else:
        even_odd_dict[num] = "Odd"

print(even_odd_dict)
