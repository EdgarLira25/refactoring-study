import pytest

from dealing_with_inheritance.extract_superclass.after import (
    CreditCardPaymentAfter,
    PixPaymentAfter,
)
from dealing_with_inheritance.extract_superclass.before import (
    CreditCardPaymentBefore,
    PixPaymentBefore,
)


@pytest.mark.parametrize("credit_card_factory", [CreditCardPaymentBefore, CreditCardPaymentAfter])
def test_credit_card_payment(credit_card_factory):
    payment = credit_card_factory(amount=100.0)

    assert payment.is_valid_amount() is True
    assert payment.processing_fee() == 3.0


@pytest.mark.parametrize("pix_factory", [PixPaymentBefore, PixPaymentAfter])
def test_pix_payment(pix_factory):
    payment = pix_factory(amount=100.0)

    assert payment.is_valid_amount() is True
    assert payment.processing_fee() == 1.0


@pytest.mark.parametrize("credit_card_factory", [CreditCardPaymentBefore, CreditCardPaymentAfter])
def test_credit_card_negative_amount(credit_card_factory):
    payment = credit_card_factory(amount=-10.0)

    assert payment.is_valid_amount() is False
    assert payment.processing_fee() == -0.3
