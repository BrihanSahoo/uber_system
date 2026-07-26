from dataclasses import dataclass
from models.driver_status import DriverStatus

@dataclass
class DriverLocation:
    driver_id: str
    latitude: float
    longitude: float
    cell_id: str
    status: DriverStatus = DriverStatus.ONLINE