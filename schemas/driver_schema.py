from pydantic import BaseModel


class DriverResponse(BaseModel):

    driver_id: str

    latitude: float

    longitude: float

    cell_id: str

    status: str