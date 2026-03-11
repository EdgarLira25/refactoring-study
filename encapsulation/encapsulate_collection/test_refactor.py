import pytest

from encapsulation.encapsulate_collection.after import (
    Client1ExampleAfter,
    Client2ExampleAfter,
    Client3ExampleAfter,
    ReadingGroupAfter,
)
from encapsulation.encapsulate_collection.before import (
    Client1ExampleBefore,
    Client2ExampleBefore,
    Client3ExampleBefore,
    ReadingGroupBefore,
)


def base_members():
    return ["Edgar", "Lia", "Caio"]


def make_group_before() -> ReadingGroupBefore:
    return ReadingGroupBefore(name="Refactoring Club", members=base_members())


def make_group_after() -> ReadingGroupAfter:
    return ReadingGroupAfter(name="Refactoring Club", members=base_members())


@pytest.mark.parametrize(
    "client1",
    [
        Client1ExampleBefore(make_group_before()),
        Client1ExampleAfter(make_group_after()),
    ],
)
def test_client1_enroll_trial_members(client1):
    new_members = ["Ana", "Bruno", "Carla"]
    client1.enroll_trial_members(new_members)
    expected = base_members() + new_members
    assert client1.group.members == expected


@pytest.mark.parametrize(
    "client2",
    [
        Client2ExampleBefore(make_group_before()),
        Client2ExampleAfter(make_group_after()),
    ],
)
def test_client2_remove_inactive_members(client2):
    client2.remove_inactive_members(["Edgar"])
    expected = base_members()
    expected.remove("Edgar")
    assert client2.group.members == expected


@pytest.mark.parametrize(
    "client3",
    [
        Client3ExampleBefore(make_group_before()),
        Client3ExampleAfter(make_group_after()),
    ],
)
def test_client3_replace_all_members(client3):
    client3.replace_all_members(["Zezinho"])
    expected = ["Zezinho"]
    assert client3.group.members == expected
