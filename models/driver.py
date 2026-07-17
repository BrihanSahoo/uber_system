from pydantic import BaseModel

class Driver(BaseModel):
    name: str

    latitude: float

    longitude: float