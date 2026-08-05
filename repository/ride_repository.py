from services.database import supabase
from supabase import Client
from models.ride_history import RideHistory
from dataclasses import asdict


class RideRepository:
    
    def __init__(self,client:Client = supabase):
        self.client = client
    
    def create_ride(self,ride:RideHistory):
        ride = asdict(ride)
        response = (
           self.client
           .table("ride_history")
           .insert(ride)
           .execute() 
        )
        if not response.data:
                return None
        return RideHistory(**response.data[0])

    def get(self,ride_id:str):
        response = (
            self.client
            .table("ride_history")
            .select("*")
            .eq("id",ride_id)
            .limit(1)
            .execute()
        )
        
        if not response.data:
            return None
        return RideHistory(**response.data[0])
        
    