"""
Example 9 from Chapter 11: Building Systems - Object-Oriented Programming
Python Programming Fundamentals by Rajesh Aadi

Bankaccount
"""

class BankAccount:
    """Bank account with protected balance"""

    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance  # Private attribute (starts with __)

    def deposit(self, amount):
        """Deposit money"""
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        """Withdraw money"""
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient funds")

        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        """Get current balance"""
        return self.__balance

# Usage
account = BankAccount("12345", 1000)

account.deposit(500)
print(account.get_balance())  # 1500

account.withdraw(200)
print(account.get_balance())  # 1300

# Cannot access private attribute directly
# print(account.__balance)  # AttributeError!

# But can use getter
print(account.get_balance())  # 1300
