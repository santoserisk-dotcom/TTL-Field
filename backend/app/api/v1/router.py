from fastapi import APIRouter

from app.api.v1 import tracking, websocket

api_router = APIRouter()
api_router.include_router(tracking.router, prefix="/tracking", tags=["tracking"])
api_router.include_router(websocket.router, prefix="/ws", tags=["websocket"])
