# Write a Python program to display all prime numbers between 0 and 50.

for num in range(1, 50):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is Prime")
