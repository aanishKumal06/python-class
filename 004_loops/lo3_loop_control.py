# break - exit the loop
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4

# continue - skip to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # Prints 0, 1, 3, 4

# 1. Print odd numbers from 1-10
for i in range(1, 11):
    if i % 2 == 1:
        print(i)

# 2. Break when finding 7
for i in range(10):
    if i == 7:
        break
    print(i)
