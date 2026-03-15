class AccountStatementServiceAfter:
    def __init__(self, customer_name: str, balance: float) -> None:
        self.customer_name = customer_name
        self.balance = balance
        self.statement_sent = False
        self.sent_count = 0

    def send_statement(self, month: str) -> str:
        return (
            f"Statement for {self.customer_name} ({month}): "
            f"balance {self.balance:.2f}"
        )

    def mark_statement_as_sent(self) -> None:
        self.sent_count += 1
        self.statement_sent = True
