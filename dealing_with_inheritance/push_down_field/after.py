class UserAfter:
    def __init__(self, name: str) -> None:
        self.name = name


class SalespersonAfter(UserAfter):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.sales_target = 100000.0

    def progress_ratio(self, sales_amount: float) -> float:
        return round(sales_amount / self.sales_target, 2)


class SupportAgentAfter(UserAfter):
    def queue_label(self) -> str:
        return f"Support queue for {self.name}"
