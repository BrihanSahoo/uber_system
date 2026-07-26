from dataclasses import dataclass
from typing import Optional
from pydantic import EmailStr

@dataclass
class Driver:
    id:int
    latitude:float
    longitude:float
    available:bool
    
@dataclass
class User:
    id:int
    latitude:float
    longitude:float
 
@dataclass
class DataBaseUser:
    id: Optional[str] = None
    username: str = ""
    email: EmailStr = ""
    hashed_password: str = ""
    phone_number: str = ""

@dataclass
class DataBaseDriver:
    id:Optional[str]=None
    username: str = ""
    email: EmailStr = ""
    hashed_password: str = ""
    phone_number: str = ""
    is_verified:bool=False

    