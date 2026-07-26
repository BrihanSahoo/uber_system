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
    
    async def get_driver(
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
        
        row = response.data[0]

        return DriverLocation(
            driver_id=row["id"],
            latitude=row["latitude"],
            longitude=row["longitude"],
            cell_id=row["h3_cell"],
            status=DriverStatus(row["status"]),
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
            .eq("status",DriverStatus.ONLINE.value)
            .in_("h3_cell",cells)
            .execute()
        )
        
        drivers = []
        
        for row in response.data:
            
            drivers.append(
                DriverLocation(
                    driver_id=row["id"],
                    latitude=row["latitude"],
                    longitude=row["longitude"],
                    cell_id=row["h3_cell"],
                    status=DriverStatus(row["status"]),
                )
            )
        return drivers
    
    
    async def reserve_driver(self,driver_id:str)->bool:
        
        response = (
            self.client.rpc(
                "reserve_driver",
                {
                    "p_driver_id":driver_id
                }
            ).execute()
        )
        
        return (response.data) is True
        
        