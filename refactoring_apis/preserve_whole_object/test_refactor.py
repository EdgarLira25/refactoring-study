import pytest

from refactoring_apis.preserve_whole_object.after import (
    ClientExampleAfter,
    HeatingControllerAfter,
)
from refactoring_apis.preserve_whole_object.before import (
    ClientExampleBefore,
    HeatingControllerBefore,
)
from refactoring_apis.preserve_whole_object.shared import RoomStatus, TemperaturePlan


def get_controller_before():
    return HeatingControllerBefore()


def get_controller_after():
    return HeatingControllerAfter()


def list_controller():
    return [get_controller_before(), get_controller_after()]


def list_client():
    return [
        ClientExampleBefore(get_controller_before()),
        ClientExampleAfter(get_controller_after()),
    ]


@pytest.mark.parametrize("controller", list_controller())
@pytest.mark.parametrize(
    "plan_min, plan_max, current, expected_heat, expected_emergency",
    [
        (18.0, 24.0, 16.0, True, False),
        (18.0, 24.0, 20.0, False, False),
        (18.0, 24.0, 31.0, False, True),
    ],
)
def test_heating_rules(
    controller: HeatingControllerBefore | HeatingControllerAfter,
    plan_min: float,
    plan_max: float,
    current: float,
    expected_heat: bool,
    expected_emergency: bool,
):
    plan = TemperaturePlan(min_temp=plan_min, max_temp=plan_max)
    room = RoomStatus(current_temp=current)

    if isinstance(controller, HeatingControllerBefore):
        should_heat = controller.requires_heating(plan.min_temp, room.current_temp)
        is_emergency = controller.is_outside_emergency_range(
            plan.min_temp,
            plan.max_temp,
            room.current_temp,
        )
    else:
        should_heat = controller.requires_heating(plan, room)
        is_emergency = controller.is_outside_emergency_range(plan, room)

    assert should_heat is expected_heat
    assert is_emergency is expected_emergency


@pytest.mark.parametrize("client", list_client())
@pytest.mark.parametrize(
    "plan, room_status, expected_heat, expected_emergency",
    [
        (
            TemperaturePlan(min_temp=18.0, max_temp=24.0),
            RoomStatus(current_temp=16.0),
            True,
            False,
        ),
        (
            TemperaturePlan(min_temp=18.0, max_temp=24.0),
            RoomStatus(current_temp=20.0),
            False,
            False,
        ),
        (
            TemperaturePlan(min_temp=18.0, max_temp=24.0),
            RoomStatus(current_temp=31.0),
            False,
            True,
        ),
    ],
)
def test_client_example_unpacks_plan_fields(
    client: ClientExampleBefore | ClientExampleAfter,
    plan: TemperaturePlan,
    room_status: RoomStatus,
    expected_heat: bool,
    expected_emergency: bool,
):
    result = client.evaluate_room(plan, room_status)
    assert result["should_heat"] is expected_heat
    assert result["is_emergency"] is expected_emergency
