from first_set_of_refactoring.combine_function_into_transform.before.order_calculators import (
    calculate_discount,
    calculate_subtotal,
    calculate_tax,
    calculate_total,
    calculate_total_items,
)


class Client1Before:

    def random_example(self, order: dict):
        subtotal = calculate_subtotal(order)
        total_items = calculate_total_items(order)

        return {
            "subtotal": subtotal,
            "total_items": total_items,
        }


class Client2Before:

    def random_example(self, order: dict):
        subtotal = calculate_subtotal(order)
        discount = calculate_discount(order)

        return {
            "subtotal": subtotal,
            "discount": discount,
        }


class Client3Before:

    def random_example(self, order: dict):
        total = calculate_total(order)
        tax = calculate_tax(order)

        return {
            "tax": tax,
            "total": total,
        }
