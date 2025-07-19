from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):

    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount):
        return f"Paid {amount}$ using Credit Card ending in {str(self.card_number)[-4:]}"


class PayPalPayment(PaymentMethod):

    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid {amount}$ using PayPal account: {self.email}"


class BitcoinPayment(PaymentMethod):

    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        return f"Paid ${amount} using Bitcoin wallet: {self.wallet_address}"
    


cc = CreditCardPayment("1234567876544", 2342)
print(cc.pay(100))

pp = PayPalPayment("example@email.com")
print(pp.pay(100))

bp = BitcoinPayment("34448593485")
print(bp.pay(100))