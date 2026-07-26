

from pydantic import EmailStr

from repository.user_repository import UserRepository
from utils.hashing import verify_password
from utils.jwt import create_access_token


async def login(email:EmailStr,password:str):
    user = await UserRepository.get_user_by_email(email)
    if user is None:
        raise Exception("No user found. Please register.")
    
    if not verify_password(password,user.hashed_password):
        raise Exception("Invalid credentials.")
    
    access_token = create_access_token(
            {
                "sub":user.id,
                "email":str(user.email)
            }
        )
        
    return {
            "access_token": access_token,
            "token_type": "bearer"
        }
    