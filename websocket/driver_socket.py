from fastapi import APIRouter,WebSocket,WebSocketDisconnect
from services.location_service import LocationService
from websocket.connection_manager import ConnectionManager

router = APIRouter()


@router.websocket("/driver")
async def driver_socket(websocket:WebSocket):
    
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            LocationService.update_driver_location(
                driver_id=data["driver_id"],
                latitude=data["latitude"],
                longitude=data["longitude"]
            )
            await websocket.send_json(
                {
                    "status":"updated"
                }
            )
    except WebSocketDisconnect:
        print("Driver disconnected.")
