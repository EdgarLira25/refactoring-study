def calculate_subtotal(order: dict) -> float:
    subtotal = 0
    for item in order["items"]:
        subtotal += item["price"] * item["quantity"]
    return subtotal


def calculate_total_items(order: dict) -> int:
    total = 0
    for item in order["items"]:
        total += item["quantity"]
    return total


def calculate_discount(order: dict) -> float:
    subtotal = calculate_subtotal(order)
    if order["customer_type"] == "premium":
        return subtotal * 0.1
    return 0


def calculate_tax(order: dict) -> float:
    subtotal = calculate_subtotal(order)
    return subtotal * 0.12


def calculate_total(order: dict) -> float:
    subtotal = calculate_subtotal(order)
    discount = calculate_discount(order)
    tax = calculate_tax(order)

    return subtotal - discount + tax
