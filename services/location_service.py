from models.driver import Driver
from services.h3_service import H3Service
from storage.memory_store import MemoryStore
from models.driver_location import DriverLocation

class LocationService:
    
    def __init__(
        self,
        store:MemoryStore,
        h3_service:H3Service
    ):
        self.store = store
        self.h3_service = h3_service
    
    def update_driver_location(self,driver_id,latitude,longitude)->DriverLocation:
        
        new_cell = self.h3_service.get_cell(
            latitude,
            longitude
        )
        
        driver = self.store.get_driver(driver_id)
        
        if driver is None:
            driver = DriverLocation(
                driver_id=driver_id,
                latitude=latitude,
                longitude=longitude,
                cell_id = new_cell
            )
            
            self.store.add_driver(driver)
            
            return driver

        
        if driver.cell_id==new_cell:
            
            self.store.update_coordinate(
                driver,
                latitude,
                longitude
            )
            
            return driver
        
        self.store.move_driver(
            driver,
            latitude,
            longitude,
            new_cell
        )
        
        return driver
    

    