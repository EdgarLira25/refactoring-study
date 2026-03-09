class OrderProcessorBefore:

    def process(self, order: str) -> float:
        parts = order.split(",")

        product = parts[0]
        quantity = int(parts[1])
        price = float(parts[2])

        subtotal = quantity * price

        if product == "laptop":
            subtotal *= 0.9

        tax = subtotal * 0.12

        return subtotal + tax
