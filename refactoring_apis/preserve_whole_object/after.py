from refactoring_apis.preserve_whole_object.shared import RoomStatus, TemperaturePlan


class HeatingControllerAfter:
    def requires_heating(self, plan: TemperaturePlan, room: RoomStatus) -> bool:
        return room.current_temp < plan.min_temp

    def is_outside_emergency_range(
        self, plan: TemperaturePlan, room: RoomStatus
    ) -> bool:
        return room.current_temp < (plan.min_temp - 5) or room.current_temp > (
            plan.max_temp + 5
        )


class ClientExampleAfter:
    def __init__(self, controller: HeatingControllerAfter) -> None:
        self.controller = controller

    def evaluate_room(self, plan: TemperaturePlan, room_status: RoomStatus) -> dict:
        return {
            "should_heat": self.controller.requires_heating(plan, room_status),
            "is_emergency": self.controller.is_outside_emergency_range(
                plan, room_status
            ),
        }
