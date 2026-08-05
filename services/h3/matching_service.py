import asyncio
import time

from services.h3.h3_service import H3Service
from storage.memory_store import MemoryStore
from utils.distance import haversine_distance
from models.driver_status import DriverStatus
from repository.driver_repository import DriverRepository
from repository.ride_repository import RideRepository
from models.ride_status import RideStatus



class MatchingService:
    
    MAX_RADIUS = 5
    def __init__(
        self,
        h3_Service:H3Service,
        store:MemoryStore,
        driver_repository:DriverRepository,
        ride_repository:RideRepository
    ):
        self.h3_service = h3_Service
        self.store = store
        self.driver_repository = driver_repository
        self.ride_repository = ride_repository
        
    
    async def dispatch_ride(self,ride_id:str):
        ride = await self.ride_repository.get(ride_id)
        drivers = await self.find_candidate_driver(
            ride.destination_lat,
            ride.destination_long
        )
        
        for driver in drivers:
            
            accepted = await self.offer_to_driver(
                ride,
                driver
            )
            
            if accepted:
                return driver
            
        await self.ride_repository.mark_no_driver_found(ride.id)
        return None
    
    async def find_candidate_drivers(
        self,
        latitude,
        longitude
    ):

        passenger_cell = self.h3_service.get_cell(
            latitude,
            longitude
        )

        for radius in range(self.MAX_RADIUS + 1):

            cells = self.h3_service.get_neighbor_cells(
                passenger_cell,
                radius
            )

            drivers = await self.driver_repository.find_online_drivers_in_cell(
                cells
            )

            if drivers:

                drivers.sort(
                    key=lambda d: haversine_distance(
                        latitude,
                        longitude,
                        d.latitude,
                        d.longitude
                    )
                )

                return drivers

        return []
    
    
    async def offer_to_driver(
        self,
        ride,
        driver
    ):

        offer = await self.offer_repository.create_offer(
            ride_id=ride.id,
            driver_id=driver.id,
            expires_in=10
        )

        await self.notification_service.send_offer(
            driver,
            ride,
            offer
        )

        accepted = await self.wait_for_driver_response(
            offer.id,
            timeout=10
        )

        if accepted:
            return True

        await self.offer_repository.mark_expired(
            offer.id
        )

        return False
    
    
    async def wait_for_driver_response(
        self,
        offer_id,
        timeout
    ):

        start = time.monotonic()

        while time.monotonic() - start < timeout:

            offer = await self.offer_repository.get(
                offer_id
            )

            if offer.status == RideStatus.ACCEPTED:
                return True

            if offer.status == RideStatus.REJECTED:
                return False

            await asyncio.sleep(0.5)

        return False
        
        
    
    async def dispatch_driver(
        self,
        latitude:float,
        longitude:float
    ):
        
        passenger_cell = self.h3_service.get_cell(latitude,longitude)
        
        for radius in range(self.MAX_RADIUS+1):
            cells = self.h3_service.get_neighbor_cells(passenger_cell,radius)
            drivers = await self.driver_repository.find_online_drivers_in_cell(cells)
            if not drivers:
                continue
            
            driver_distances = []
            
            for driver in drivers:
                distance = haversine_distance(
                    latitude,
                    longitude,
                    driver.latitude,
                    driver.longitude
                )
                
                driver_distances.append(
                    (
                        driver,
                        distance
                    )
                )
            driver_distances.sort(
                key=lambda item:item[1]
            )
            
            for driver,_ in driver_distances:
                reserved = await self.driver_repository.reserve_driver(driver.id)
                if reserved:
                    return driver
        

    def find_best_driver_in_cells(
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

        passenger_cell = self.h3_service.get_cell(
        latitude,
        longitude,
        )

        for radius in range(self.MAX_RADIUS + 1):

            candidate_cells = self.h3_service.get_neighbor_cells(
                passenger_cell,
                radius,
            )

            driver = self.find_best_driver_in_cells(
                candidate_cells,
                latitude,
                longitude,
            )

            if driver is not None:
                return driver

        return None


matching_service = MatchingService()
        
        
    