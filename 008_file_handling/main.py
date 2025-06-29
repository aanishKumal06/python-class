try:
    num = 45
    print("Number divided by 0", num / 0)

except ZeroDivisionError as e:
    print(e)
    print(e.__class__.__name__)
