import pytest

from refactoring_apis.replace_command_with_function.after import GreetingServiceAfter
from refactoring_apis.replace_command_with_function.before import (
    GreetingServiceBefore,
)


def list_service():
    return [GreetingServiceBefore(), GreetingServiceAfter()]


@pytest.mark.parametrize("service", list_service())
@pytest.mark.parametrize(
    "name, is_formal, expected",
    [
        ("Bia", True, "Hello, Bia. Welcome back."),
        ("Bia", False, "Hi Bia!"),
    ],
)
def test_greeting_service(
    service: GreetingServiceBefore | GreetingServiceAfter,
    name: str,
    is_formal: bool,
    expected: str,
):
    assert service.build_greeting(name=name, is_formal=is_formal) == expected
