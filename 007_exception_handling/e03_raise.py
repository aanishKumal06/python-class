# Custom exception class
divisor = int(input("Enter a number: "))
dividend = 20

if divisor == 0:
    error_msg = "Jpt number na hanana"
    raise Exception(error_msg)

result = dividend / divisor
print("The result is ", result)
