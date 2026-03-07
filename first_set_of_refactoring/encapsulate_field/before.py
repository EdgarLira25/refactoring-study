class BankAccountBefore:

    def __init__(self, balance: float):
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount

    def apply_monthly_fee(self):
        self.balance -= 10
