from models.ride_status import RideStatus
class RideHistory:
    id:str
    rider_id:str
    user_id:str
    
    source_name:str
    destination_name:str
    
    # Latitude
    source_lat:float
    destination_lat:float
    
    #Longitude
    source_long:float
    destination_long:float
    
    cost:float
    distance:float
    
    status:RideStatus = RideStatus.SEARCHING
    