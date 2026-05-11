from fastapi import APIRouter, WebSocket

router = APIRouter()


@router.websocket("/operations")
async def operations_socket(ws: WebSocket) -> None:
    await ws.accept()
    await ws.send_json({"event": "connected", "channel": "operations"})
    await ws.close()
