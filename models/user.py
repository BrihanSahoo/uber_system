from dataclasses import dataclass

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