from services.h3_service import H3Service
from storage.memory_store import MemoryStore
from utils.distance import haversine_distance
from models.driver_status import DriverStatus
from repository.driver_repository import DriverRespository

MAX_RADIUS = 5

class MatchingService:
    def __init__(
        self,
        h3_Service:H3Service,
        store:MemoryStore
    ):
        self.h3_service = h3_Service
        self.store = store
        
        

    def _find_best_driver_in_cells(
        self,
        cells: list[str],
        passenger_lat: float,
        passenger_lon: float,
    ):

        candidate_driver_ids = set()

        for cell in cells:
            candidate_driver_ids.update(
                self.store.get_drivers_in_cell(cell)
            )

        best_driver = None
        best_distance = float("inf")

        for driver_id in candidate_driver_ids:

            driver = self.store.get_driver(driver_id)

            if driver is None:
                continue
            
            if driver.status != DriverStatus.ONLINE:
                continue
            distance = haversine_distance(
                passenger_lat,
                passenger_lon,
                driver.latitude,
                driver.longitude,
            )

            if distance < best_distance:
                best_distance = distance
                best_driver = driver

        return best_driver
    
    def find_nearest_driver(
        self,
        latitude: float,
        longitude: float,
    ):

        passenger_cell = self.h3.get_cell(
        latitude,
        longitude,
        )

        for radius in range(MAX_RADIUS + 1):

            candidate_cells = self.h3.get_neighbor_cells(
                passenger_cell,
                radius,
            )

            driver = self._find_best_driver_in_cells(
                candidate_cells,
                latitude,
                longitude,
            )

            if driver is not None:
                return driver

        return None
        
        
    