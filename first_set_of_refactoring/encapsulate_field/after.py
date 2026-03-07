class Balance:
    def __init__(self, balance: float) -> None:
        self._value = balance

    @property
    def value(self) -> float:
        return self._value

    def add(self, amount: float):
        new_value = self._value + amount
        if new_value < 0:
            raise ValueError("Balance cannot be negative")
        self._value = new_value


class BankAccountAfter:

    def __init__(self, balance: float):
        self._balance = Balance(balance)

    @property
    def balance(self):
        return self._balance.value

    def deposit(self, amount: float):
        self._balance.add(amount)

    def withdraw(self, amount: float):
        self._balance.add(-amount)

    def apply_monthly_fee(self):
        self._balance.add(-10)
