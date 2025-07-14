class Account:
    def __init__(self, name, balance):
        self.name = name              # public attribute
        self.__balance = balance       # private attribute
        self._bank = "ATM"

    def get_balance(self):
        return self.__balance
    
    def save_money(self, amount):     # public method
        self.__add_money(amount)
    
    def __add_money(self, amount):    # private method
        self.__balance += amount



account = Account("Martian", 2000)
print(account.name)
print(account.get_balance())
print(account._bank)
account.save_money(2000)
print(account.get_balance())