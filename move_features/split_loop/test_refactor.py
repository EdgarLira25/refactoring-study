import pytest

from move_features.split_loop.after import SalesAnalyzerAfter
from move_features.split_loop.before import SalesAnalyzerBefore


@pytest.fixture()
def orders() -> list[dict]:
    return [
        {"customer_id": 1, "price": 500.0, "quantity": 1, "status": "paid"},
        {"customer_id": 2, "price": 300.0, "quantity": 4, "status": "paid"},
        {"customer_id": 1, "price": 200.0, "quantity": 2, "status": "pending"},
    ]


@pytest.mark.parametrize("analyzer", [SalesAnalyzerBefore(), SalesAnalyzerAfter()])
def test_metrics(
    analyzer: SalesAnalyzerBefore | SalesAnalyzerAfter, orders: list[dict]
):
    assert analyzer.metrics(orders) == {
        "total_revenue": 2100.0,
        "high_value_orders": 1,
        "active_customers": 2,
    }


@pytest.mark.parametrize("analyzer", [SalesAnalyzerBefore(), SalesAnalyzerAfter()])
def test_metrics_with_empty_orders(analyzer: SalesAnalyzerBefore | SalesAnalyzerAfter):
    assert analyzer.metrics([]) == {
        "total_revenue": 0.0,
        "high_value_orders": 0,
        "active_customers": 0,
    }
