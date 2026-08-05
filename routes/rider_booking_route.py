from fastapi import APIRouter, Depends, HTTPException

from services.h3.matching_service import MatchingService
from dependencies import get_matching_service


router = APIRouter(
    prefix="/riders",
    tags=["Rider Booking"]
)


@router.post("/book")
async def book_ride(
    dest_latitude:float,
    dest_longitude:float,
    latitude: float,
    longitude: float,
    matching_service: MatchingService = Depends(get_matching_service),
    
):

    driver = await matching_service.dispatch_driver(
        latitude=latitude,
        longitude=longitude
    )

    if driver is None:
        raise HTTPException(
            status_code=404,
            detail="No driver available"
        )

    return {
        "message": "Driver assigned",
        "driver_id": driver.id,
        "latitude": driver.latitude,
        "longitude": driver.longitude
    }