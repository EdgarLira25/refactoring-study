from datetime import date
import pytest

from encapsulation.extract_class.after import CustomerProfileAfter
from encapsulation.extract_class.before import CustomerProfileBefore


def get_customer_profile_before():
    return CustomerProfileBefore(
        name="Teste",
        email="teste@email.com",
        phone="+55 11 99999-0000",
        street="Av. Teste, 1000",
        city="Sao Paulo",
        state="SP",
        postal_code="01310-100",
        country="BR",
        subscription_plan="pro",
        monthly_fee=200.0,
        last_payment_date="2026-02-01",
    )


def get_customer_profile_after():
    return CustomerProfileAfter(
        name="Teste",
        email="teste@email.com",
        phone="+55 11 99999-0000",
        street="Av. Teste, 1000",
        city="Sao Paulo",
        state="SP",
        postal_code="01310-100",
        country="BR",
        subscription_plan="pro",
        monthly_fee=200.0,
        last_payment_date="2026-02-01",
    )


type Profiles = CustomerProfileAfter | CustomerProfileBefore


def list_customer_profiles():
    return [get_customer_profile_before(), get_customer_profile_after()]


@pytest.mark.parametrize("customer_profile", list_customer_profiles())
def test_contact_card(customer_profile: Profiles):
    assert (
        customer_profile.contact_card() == "Teste | teste@email.com | +55 11 99999-0000"
    )


@pytest.mark.parametrize("customer_profile", list_customer_profiles())
def test_shipping_label(customer_profile: Profiles):
    assert customer_profile.shipping_label() == (
        "Teste\n" "Av. Teste, 1000\n" "Sao Paulo - SP, 01310-100\n" "BR"
    )


@pytest.mark.parametrize("customer_profile", list_customer_profiles())
def test_update_address(customer_profile: Profiles):
    customer_profile.update_address(
        street="Rua Augusta, 500",
        city="Sao Paulo",
        state="SP",
        postal_code="01305-000",
        country="BR",
    )
    if isinstance(customer_profile, CustomerProfileBefore):
        street = customer_profile.street
        city = customer_profile.city
        state = customer_profile.state
        postal_code = customer_profile.postal_code
        country = customer_profile.country
    elif isinstance(customer_profile, CustomerProfileAfter):
        street = customer_profile.address.street
        city = customer_profile.address.city
        state = customer_profile.address.state
        postal_code = customer_profile.address.postal_code
        country = customer_profile.address.country

    assert street == "Rua Augusta, 500"
    assert city == "Sao Paulo"
    assert state == "SP"
    assert postal_code == "01305-000"
    assert country == "BR"


@pytest.mark.parametrize("customer_profile", list_customer_profiles())
@pytest.mark.parametrize(
    "country, expected",
    [
        ("US", 214.0),
        ("BR", 224.0),
    ],
)
def test_monthly_charge_preview(
    customer_profile: Profiles, country: str, expected: float
):
    if isinstance(customer_profile, CustomerProfileBefore):
        customer_profile.country = country
    elif isinstance(customer_profile, CustomerProfileAfter):
        customer_profile.address.country = country
    preview = customer_profile.monthly_charge_preview()

    assert preview == expected


@pytest.mark.parametrize("customer_profile", list_customer_profiles())
@pytest.mark.parametrize(
    "today, expected_overdue",
    [(date(2026, 2, 20), False), (date(2026, 3, 5), True)],
)
def test_is_payment_overdue(
    customer_profile: Profiles, today: date, expected_overdue: bool
):
    is_payment_overdue = customer_profile.is_payment_overdue(today)
    assert is_payment_overdue is expected_overdue


@pytest.mark.parametrize("customer_profile", list_customer_profiles())
def test_mark_payment_received(customer_profile: Profiles):
    payment_date = date(2026, 3, 11)
    customer_profile.mark_payment_received(payment_date)
    if isinstance(customer_profile, CustomerProfileBefore):
        last_payment = customer_profile.last_payment_date
    elif isinstance(customer_profile, CustomerProfileAfter):
        last_payment = customer_profile.subscription.last_payment_date
    assert last_payment == "2026-03-11"
