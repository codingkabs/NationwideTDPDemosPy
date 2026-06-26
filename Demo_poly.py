class Payment:
    def pay(self, amount):
        pass

class PayPal(Payment):
    def pay(self, amount):
        print(f"Paid £{amount} via PayPal")

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid £{amount} via Credit Card")

class ApplePay(Payment):
    def pay(self, amount):
        print(f"Paid £{amount} via Apple Pay")

def checkout(payment, amount):
    payment.pay(amount)

checkout(CreditCard(), 100)
checkout(PayPal(), 100)
checkout(ApplePay(), 100)