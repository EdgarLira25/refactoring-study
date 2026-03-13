from datetime import datetime
import pytest
from move_features.move_statements_to_callers.after import BillingServiceAfter
from move_features.move_statements_to_callers.before import BillingServiceBefore
from move_features.move_statements_to_callers.shared import Person, Photo, Stream


def list_billing_services():
    return [BillingServiceBefore(), BillingServiceAfter()]


@pytest.fixture()
def stream() -> Stream:
    return Stream()


@pytest.mark.parametrize("billing_service", list_billing_services())
def test_render_person(
    billing_service: BillingServiceBefore | BillingServiceAfter, stream: Stream
):
    person = Person(name="Teste")
    billing_service.render_person(stream, person)
    assert stream.text == "<p>Teste</p>\n"


@pytest.mark.parametrize("billing_service", list_billing_services())
def test_render_photo(
    billing_service: BillingServiceBefore | BillingServiceAfter, stream: Stream
):
    photo = Photo(
        title="Road Trip",
        date=datetime(2026, 2, 1),
        location="Sao Paulo",
    )

    billing_service.render_photo(stream, photo)

    assert stream.text == (
        "<p>title: Road Trip</p>\n"
        "<p>date: 2026-02-01 00:00:00</p>\n"
        "<p>location: Sao Paulo</p>\n"
    )


@pytest.mark.parametrize("billing_service", list_billing_services())
@pytest.mark.parametrize(
    "photos, expected",
    [
        (
            [
                Photo("Old", datetime(2025, 12, 31), "NY"),
                Photo("New", datetime(2026, 1, 1), "SF"),
            ],
            (
                "<div>\n"
                "<p>title: New</p>\n"
                "<p>date: 2026-01-01 00:00:00</p>\n"
                "<p>location: SF</p>\n"
                "</div>\n"
            ),
        ),
        (
            [Photo("Future", datetime(2026, 4, 10), "Rio")],
            (
                "<div>\n"
                "<p>title: Future</p>\n"
                "<p>date: 2026-04-10 00:00:00</p>\n"
                "<p>location: Rio</p>\n"
                "</div>\n"
            ),
        ),
    ],
)
def test_list_recent_photos(
    billing_service: BillingServiceBefore | BillingServiceAfter,
    stream: Stream,
    photos: list[Photo],
    expected: str,
):
    billing_service.list_recent_photos(stream, photos)

    assert stream.text == expected
