class ProductCatalogAfter:
    def discounted_total(self, products: list[dict], min_stock: int = 1) -> float:
        eligible_products = filter(
            lambda product: product["active"] and product["stock"] >= min_stock,
            products,
        )
        discounted_prices = map(
            lambda product: product["price"] * (1 - product["discount_percent"] / 100),
            eligible_products,
        )
        return round(sum(discounted_prices), 2)

    def active_names(self, products: list[dict]) -> list[str]:
        active_products = filter(lambda product: product["active"], products)
        normalized_names = map(
            lambda product: product["name"].strip().lower(),
            active_products,
        )
        return list(normalized_names)
