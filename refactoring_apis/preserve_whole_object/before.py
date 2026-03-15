from refactoring_apis.preserve_whole_object.shared import RoomStatus, TemperaturePlan


class HeatingControllerBefore:
    def requires_heating(
        self,
        plan_min_temp: float,
        current_temp: float,
    ) -> bool:
        return current_temp < plan_min_temp

    def is_outside_emergency_range(
        self,
        plan_min_temp: float,
        plan_max_temp: float,
        current_temp: float,
    ) -> bool:
        return current_temp < (plan_min_temp - 5) or current_temp > (plan_max_temp + 5)


class ClientExampleBefore:
    def __init__(self, controller: HeatingControllerBefore) -> None:
        self.controller = controller

    def evaluate_room(self, plan: TemperaturePlan, room_status: RoomStatus) -> dict:
        should_heat = self.controller.requires_heating(
            plan.min_temp,
            room_status.current_temp,
        )
        is_emergency = self.controller.is_outside_emergency_range(
            plan.min_temp,
            plan.max_temp,
            room_status.current_temp,
        )
        return {"should_heat": should_heat, "is_emergency": is_emergency}
