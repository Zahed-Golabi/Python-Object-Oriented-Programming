class BankAccount:

    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.__balance += amount
        return f"Deposited {amount}. New balance: {self.__balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.__balance:
            return f"Insufficient funds. Current balance: {self.__balance}"
        self.__balance -= amount
        return f"Withdrew {amount}. New balance: {self.__balance}"

    def get_balance(self):
        return self.__balance
        
    def get_account_number(self):
        return self.__account_number


# Test
acc1 = BankAccount(1237654, 200)
print(acc1.deposit(100))         # Deposited 100
print(acc1.get_balance())        # 300
print(acc1.withdraw(200))        # Withdrew 200
print(acc1.get_balance())        # 100
print(acc1.get_account_number()) # 1237654
print(acc1.withdraw(400))        # Insufficient funds
