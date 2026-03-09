class InvoiceCalculatorBefore:

    def calculate(self, order: dict) -> float:
        t = 0
        c = order["customer"]["type"]

        for i in order["items"]:
            t += i["price"] * i["quantity"]

        if c == "premium":
            t = t * 0.9

        return t
