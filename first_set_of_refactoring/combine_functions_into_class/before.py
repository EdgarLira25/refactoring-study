def calculate_subtotal(items: list[dict]) -> float:
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


def calculate_discount(customer_type: str, subtotal: float) -> float:
    if customer_type == "premium":
        return subtotal * 0.1
    return 0


def calculate_total(items: list[dict], customer_type: str) -> float:
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(customer_type, subtotal)

    return subtotal - discount
