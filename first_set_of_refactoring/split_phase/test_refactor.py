import pytest

from first_set_of_refactoring.split_phase.after import OrderProcessorAfter
from first_set_of_refactoring.split_phase.before import OrderProcessorBefore


@pytest.mark.parametrize(
    "order_processor", [OrderProcessorBefore(), OrderProcessorAfter()]
)
def test_split_phase(order_processor):
    assert order_processor.process("laptop,2,3000") == 6048.0
