class ProductCatalogBefore:
    def discounted_total(self, products: list[dict], min_stock: int = 1) -> float:
        eligible_total = 0.0

        for product in products:
            if not product["active"]:
                continue

            if product["stock"] < min_stock:
                continue

            discounted_price = product["price"] * (1 - product["discount_percent"] / 100)
            eligible_total += discounted_price

        return round(eligible_total, 2)

    def active_names(self, products: list[dict]) -> list[str]:
        names = []
        for product in products:
            if product["active"]:
                names.append(product["name"].strip().lower())
        return names
