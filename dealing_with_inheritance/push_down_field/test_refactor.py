import pytest

from dealing_with_inheritance.push_down_field.after import SalespersonAfter, SupportAgentAfter
from dealing_with_inheritance.push_down_field.before import (
    SalespersonBefore,
    SupportAgentBefore,
)


@pytest.mark.parametrize("salesperson_factory", [SalespersonBefore, SalespersonAfter])
def test_salesperson_uses_sales_target(salesperson_factory):
    salesperson = salesperson_factory(name="Ana")

    assert salesperson.sales_target == 100000.0
    assert salesperson.progress_ratio(50000.0) == 0.5


@pytest.mark.parametrize("support_factory", [SupportAgentBefore, SupportAgentAfter])
def test_support_agent_behavior(support_factory):
    support_agent = support_factory(name="Bia")

    assert support_agent.queue_label() == "Support queue for Bia"
