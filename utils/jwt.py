from datetime import datetime,timedelta,timezone
from fastapi import Depends, HTTPException,status
from jose import jwt,JWTError
from config import settings

from fastapi.security import OAuth2PasswordBearer

from repository.user_repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
def create_access_token(data:dict):
    encode_data = data.copy()
    
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    
    encode_data.update({"exp": expire})
    
    return jwt.encode(encode_data,settings.SECRET_KEY,algorithm=settings.ALGORITHM)

async def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        
        
        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired access token."
            )
        
        user_id = payload.get("sub")
        
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token"
            )
        user = await UserRepository.get_user_by_id(
            int(user_id)
        )
        
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User no longer exists"
            )
        return user
    except JWTError:
        return None
        
    
            