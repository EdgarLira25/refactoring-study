from dataclasses import dataclass


@dataclass
class TemperaturePlan:
    min_temp: float
    max_temp: float


@dataclass
class RoomStatus:
    current_temp: float
