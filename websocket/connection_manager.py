from fastapi import WebSocket


class ConnectionManager:
    
    def __init__(self):
        self.driver_connections = {}
    
    async def connect_driver(
        self,
        driver_id:str,
        websocket:WebSocket
    ):
        await websocket.accept()
        self.driver_connections[driver_id] = websocket
    
    async def disconnect_driver(
        self,
        driver_id:str
    ):
        self.driver_connections.pop( driver_id,None) # Delete if exists
    
    async def send_to_driver(self,driver_id:str,message:dict):
        websocket = self.driver_connections.get(driver_id)
        if websocket:
            await websocket.send_json(message)