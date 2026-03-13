import pytest

from move_features.replace_loop_with_pipeline.after import ProductCatalogAfter
from move_features.replace_loop_with_pipeline.before import ProductCatalogBefore


@pytest.fixture()
def products() -> list[dict]:
    return [
        {
            "name": " Laptop ",
            "price": 3000.0,
            "discount_percent": 10,
            "stock": 5,
            "active": True,
        },
        {
            "name": "Mouse",
            "price": 100.0,
            "discount_percent": 0,
            "stock": 0,
            "active": True,
        },
        {
            "name": "Keyboard",
            "price": 200.0,
            "discount_percent": 20,
            "stock": 10,
            "active": False,
        },
    ]


@pytest.mark.parametrize("catalog", [ProductCatalogBefore(), ProductCatalogAfter()])
def test_discounted_total(catalog: ProductCatalogBefore | ProductCatalogAfter, products: list[dict]):
    assert catalog.discounted_total(products, min_stock=1) == 2700.0


@pytest.mark.parametrize("catalog", [ProductCatalogBefore(), ProductCatalogAfter()])
def test_discounted_total_with_strict_stock(
    catalog: ProductCatalogBefore | ProductCatalogAfter, products: list[dict]
):
    assert catalog.discounted_total(products, min_stock=6) == 0.0


@pytest.mark.parametrize("catalog", [ProductCatalogBefore(), ProductCatalogAfter()])
def test_active_names(catalog: ProductCatalogBefore | ProductCatalogAfter, products: list[dict]):
    assert catalog.active_names(products) == ["laptop", "mouse"]
