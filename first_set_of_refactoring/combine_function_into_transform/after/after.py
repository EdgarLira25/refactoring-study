from first_set_of_refactoring.combine_function_into_transform.after.enrich_order import (
    EnrichOrder,
)


class Client1After:

    def __init__(self, enrich_order: EnrichOrder) -> None:
        self.enrich_order = enrich_order

    def random_example(self, order: dict):
        enriched_order = self.enrich_order.enrich_order(order)
        return {
            "subtotal": enriched_order.subtotal_price,
            "total_items": enriched_order.total_items,
        }


class Client2After:
    def __init__(self, enrich_order: EnrichOrder) -> None:
        self.enrich_order = enrich_order

    def random_example(self, order: dict):
        enriched_order = self.enrich_order.enrich_order(order)

        return {
            "subtotal": enriched_order.subtotal_price,
            "discount": enriched_order.discount,
        }


class Client3After:

    def __init__(self, enrich_order: EnrichOrder) -> None:
        self.enrich_order = enrich_order

    def random_example(self, order: dict):
        enriched_order = self.enrich_order.enrich_order(order)
        return {
            "tax": enriched_order.tax,
            "total": enriched_order.total_price,
        }
