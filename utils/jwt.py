from datetime import datetime,timedelta,timezone
from jose import jwt
from config import settings


def create_access_token(data:dict):
    encode_data = data.copy()
    
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    
    encode_data.update({"exp": expire})
    
    return jwt.encode(encode_data,settings.SECRET_KEY,algorithm=settings.ALGORITHM)