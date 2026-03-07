class ShippingCalculatorBefore:

    def calculate_shipping(self, order: dict) -> float:

        items_total = sum(item["price"] * item["quantity"] for item in order["items"])

        shipping_cost = 0

        if items_total > 500:
            shipping_cost = 0
        else:
            shipping_cost = 20

        total_shipping = shipping_cost

        return total_shipping
