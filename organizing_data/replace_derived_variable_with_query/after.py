class AccountAfter:
    def __init__(self, owner: str):
        self.owner = owner
        self.transactions: list[float] = []

    @property
    def balance(self) -> float:
        return sum(self.transactions)

    def add_transaction(self, amount: float):
        self.transactions.append(amount)

    def remove_transaction(self, amount: float):
        self.transactions.remove(amount)

    def apply_monthly_fee(self, fee: float):
        self.transactions.append(-fee)

    def summary(self) -> str:
        return f"{self.owner} balance: ${self.balance:.2f}"
