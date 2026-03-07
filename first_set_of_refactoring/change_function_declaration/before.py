class OrderServiceBefore:

    def process(self, order: dict, send_email: bool = True) -> dict:
        total = self.calc(order["items"])
        discount = self.discount(order["customer"]["type"], total)
        final_total = total - discount

        order["total"] = final_total

        if send_email:
            self.notify(order["customer"]["email"], final_total)

        return order

    def calc(self, items: list[dict]) -> float:
        total = 0
        for item in items:
            total += item["price"] * item["quantity"]
        return total

    def discount(self, customer_type: str, total: float) -> float:
        if customer_type == "premium":
            return total * 0.1
        return 0

    def notify(self, email: str, total: float):
        return f"Sending email to {email} with total {total}"
