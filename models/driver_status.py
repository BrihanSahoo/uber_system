from enum import Enum

class DriverStatus(str,Enum):
    
    OFFLINE = "OFFLINE"
    
    ONLINE = "ONLINE"
    
    BUSY = "BUSY"
    
    RESERVED = "RESERVED"