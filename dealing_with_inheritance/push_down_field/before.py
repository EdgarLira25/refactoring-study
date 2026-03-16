class UserBefore:
    def __init__(self, name: str) -> None:
        self.name = name
        self.sales_target = 100000.0


class SalespersonBefore(UserBefore):
    def progress_ratio(self, sales_amount: float) -> float:
        return round(sales_amount / self.sales_target, 2)


class SupportAgentBefore(UserBefore):
    def queue_label(self) -> str:
        return f"Support queue for {self.name}"
