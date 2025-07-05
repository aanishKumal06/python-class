def average_function(*args: int) -> float:
    average = sum(args) / len(args)
    return average


print(average_function(1, 2, 3, 3, 4, 4, 5))
