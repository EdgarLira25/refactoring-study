import pytest

from refactoring_apis.separate_query_from_modifier.after import (
    AccountStatementServiceAfter,
)
from refactoring_apis.separate_query_from_modifier.before import (
    AccountStatementServiceBefore,
)


def list_service_class():
    return [
        AccountStatementServiceBefore,
        AccountStatementServiceAfter,
    ]


Accounts = type[AccountStatementServiceBefore] | type[AccountStatementServiceAfter]


@pytest.mark.parametrize("service_class", list_service_class())
def test_send_statement_returns_content_and_marks_sent(service_class: Accounts):
    month = "2026-03"
    service = service_class("Ana", 1250.5)
    if isinstance(service, AccountStatementServiceBefore):
        message = service.send_statement_and_mark_sent(month)
    elif isinstance(service, AccountStatementServiceAfter):
        message = service.send_statement(month)
        service.mark_statement_as_sent()
    else:
        raise AssertionError("Invalid Account")
    assert message == "Statement for Ana (2026-03): balance 1250.50"


@pytest.mark.parametrize("service_class", list_service_class())
@pytest.mark.parametrize("month", ["2026-03", "2026-04", "2026-05"])
def test_send_statement_increments_count(service_class: Accounts, month: str):
    service = service_class("Ana", 1250.5)
    if isinstance(service, AccountStatementServiceBefore):
        service.send_statement_and_mark_sent(month)
    elif isinstance(service, AccountStatementServiceAfter):
        service.mark_statement_as_sent()

    assert service.sent_count == 1
