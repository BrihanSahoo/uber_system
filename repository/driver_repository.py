from services.database import supabase
from supabase import Client
from models.driver_location import DriverLocation
from models.driver_status import DriverStatus



class DriverRespository:
    
    def __init__(
        self,
        client:Client = supabase
    ):
        self.client = client
    
    async def get_drivers(
        self,
        driver_id:str
    ):
        response = (
            self.client
            .table("drivers")
            .select("*")
            .eq("id",driver_id)
            .limit(1)
            .execute()
        )
        
        if not response.data:
            return None
        
        return DriverLocation.model_validate(
            response.data[0]
        )
    
    async def find_online_drivers_in_cell(
        self,
        cells:list[str]
    )->list[DriverLocation]:
        
        if not cells:
            return []
        
        response = (
            self.client
            .table("drivers")
            .select("*")
            .eq("status",DriverStatus.ONLINE)
            .in_("h3_cell",cells)
            .execute()
        )
        
        drivers = []
        
        for row in response.data:
            
            drivers.append(
                DriverLocation.model_validate(
                    row
                )
            )
        return drivers
        
        