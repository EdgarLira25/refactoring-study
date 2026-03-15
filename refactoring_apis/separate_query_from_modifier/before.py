class AccountStatementServiceBefore:
    def __init__(self, customer_name: str, balance: float) -> None:
        self.customer_name = customer_name
        self.balance = balance
        self.statement_sent = False
        self.sent_count = 0

    def send_statement_and_mark_sent(self, month: str) -> str:
        self.statement_sent = True
        self.sent_count += 1
        return (
            f"Statement for {self.customer_name} ({month}): "
            f"balance {self.balance:.2f}"
        )
