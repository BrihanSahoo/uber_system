from enum import Enum

class RideStatus(str,Enum):
    
    SEARCHING = "SEARCHING"
    OFFER_SENT = "OFFER_SENT"
    ACCEPTED = "ACCEPTED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"