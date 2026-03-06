from datetime import datetime


class OrderProcessorBefore:

    def process_order(self, order):
        total = 0

        for item in order["items"]:
            price = item["price"]
            quantity = item["quantity"]

            subtotal = price * quantity

            if item.get("category") == "electronics":
                subtotal *= 1.10

            if quantity > 10:
                subtotal *= 0.95

            total += subtotal

        if order["customer"]["type"] == "premium":
            total *= 0.90

        shipping = 0

        if total > 500:
            shipping = 0
        else:
            if order["customer"]["country"] == "BR":
                shipping = 20
            else:
                shipping = 50

        tax = 0

        if order["customer"]["country"] == "BR":
            tax = total * 0.12
        else:
            tax = total * 0.20

        final_total = total + shipping + tax

        order["processed_at"] = datetime(2026, 1, 1).isoformat()
        order["final_total"] = final_total

        if final_total > 1000:
            order["priority"] = "high"
        else:
            order["priority"] = "normal"

        return order
