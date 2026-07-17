from collections import defaultdict

from models.driver_location import DriverLocation

class MemoryStore:
    
    def __init__(self):
        self.cell_drivers = defaultdict(set)
        self.drivers = {}
        
    def add_driver(self,driver:DriverLocation)->None:        
        self.drivers[driver.driver_id] = driver
        
        self.cell_drivers[driver.cell_id].add(driver.driver_id)
        
        
        
    
    def get_driver(self,driver_id:str) -> DriverLocation:
        
        return self.drivers.get(driver_id)
    
    
    
    def update_coordinate(
        self,
        
        driver:DriverLocation,
        
        latitude:float,
        
        longitude:float
    ):
        driver.latitude = latitude
        driver.longitude = longitude
    
    
    def move_driver(
        self,
        
        driver:DriverLocation,
        
        latitude:float,
        
        longitude:str,
        
        new_cell:str
    ):
        old_cell = driver.cell_id
        
        self.cell_drivers[old_cell].remove(driver.driver_id)
        
        if not self.cell_drivers[old_cell]:
            del self.cell_drivers[old_cell]
        
        self.cell_drivers[
            new_cell
        ].add(driver.driver_id)
        
        driver.latitude = latitude
        
        driver.longitude = longitude
        
        driver.cell_id = new_cell
    
    
    def get_drivers_in_cell(

        self,

        cell_id: str

    ) -> set[str]:

        return self.cell_drivers.get(
            cell_id,
            set()
        )