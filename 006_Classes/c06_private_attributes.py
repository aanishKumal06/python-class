
class SecureAccount:
    def __init__(self, name):
        self.name = name
        self.__balance = 0  # Private attribute (starts with __)

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited: Rs. {self.__balance}"

    def get_balance(self):
        return f"Your balance: Rs. {self.__balance}"


account = SecureAccount("TH")
print(account.deposit(1000))
print(account.get_balance())

# This won't work - private attributes can't be accessed directly
# print(account.__balance)  # AttributeError
