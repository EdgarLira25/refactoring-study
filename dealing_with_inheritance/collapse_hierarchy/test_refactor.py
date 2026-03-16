import pytest

from dealing_with_inheritance.collapse_hierarchy.after import (
    NotificationAfter,
)
from dealing_with_inheritance.collapse_hierarchy.before import (
    EmailNotificationBefore,
    NotificationBefore,
)


@pytest.mark.parametrize(
    "notification_factory", [NotificationBefore, NotificationAfter]
)
def test_notifications(notification_factory):
    notification = notification_factory(message="System updated")
    assert notification.send() == "Notify: System updated"


@pytest.mark.parametrize("email_factory", [EmailNotificationBefore, NotificationAfter])
def test_email_notifications(email_factory):
    email_notification = email_factory(message="Email sent")
    assert email_notification.send() == "Notify: Email sent"
