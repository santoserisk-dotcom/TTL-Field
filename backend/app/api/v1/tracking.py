from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel, Field


class PositionIn(BaseModel):
    technician_id: int
    device_id: str = Field(min_length=8, max_length=128)
    latitude: float
    longitude: float
    speed_kmh: float = Field(ge=0)
    battery_level: int = Field(ge=0, le=100)
    captured_at: datetime


class PositionOut(PositionIn):
    id: int


router = APIRouter()


@router.post("/positions", response_model=PositionOut)
async def ingest_position(payload: PositionIn) -> PositionOut:
    return PositionOut(id=1, **payload.model_dump())
