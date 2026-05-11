from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class UserRole(StrEnum):
    ADMIN = "admin"
    SUPERVISOR = "supervisor"
    TECHNICIAN = "technician"


class AlertType(StrEnum):
    SPEEDING = "speeding"
    DEVICE_OFFLINE = "device_offline"
    GEOFENCE_EXIT = "geofence_exit"
    LOW_BATTERY = "low_battery"


@dataclass(slots=True)
class PositionPoint:
    technician_id: int
    device_id: str
    latitude: float
    longitude: float
    speed_kmh: float
    battery_level: int
    captured_at: datetime
