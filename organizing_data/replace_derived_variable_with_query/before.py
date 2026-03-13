class AccountBefore:
    def __init__(self, owner: str):
        self.owner = owner
        self.transactions: list[float] = []
        self.balance = 0.0

    def add_transaction(self, amount: float):
        self.transactions.append(amount)
        self.balance += amount

    def remove_transaction(self, amount: float):
        self.transactions.remove(amount)
        self.balance -= amount

    def apply_monthly_fee(self, fee: float):
        self.transactions.append(-fee)
        self.balance -= fee

    def summary(self) -> str:
        return f"{self.owner} balance: ${self.balance:.2f}"
