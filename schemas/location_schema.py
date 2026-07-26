from pydantic import BaseModel, Field


class DriverLocationRequest(BaseModel):

    driver_id: str = Field(
        ...,
        description="Unique driver id"
    )

    latitude: float = Field(
        ...,
        ge=-90,
        le=90
    )

    longitude: float = Field(
        ...,
        ge=-180,
        le=180
    )