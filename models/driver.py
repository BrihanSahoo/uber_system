from pydantic import BaseModel,EmailStr

class Driver(BaseModel):
    id:str
    username:str
    email:EmailStr
    hashed_password:str
    phone_number:str
    is_verified:bool=False
    avg_rating:float
    ride_history:list[str]