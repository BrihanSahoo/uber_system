from models.user import DataBaseUser
from utils.hashing import hash_password
from utils.jwt import create_access_token
from repository.user_repository import UserRepository
from pydantic import EmailStr
from events.events import publish_event


async def register(user:DataBaseUser):
    user.hashed_password = hash_password(password=user.hashed_password)
    response = await UserRepository.get_user_by_email(user.email)
    if response:
        raise Exception("Email already exists.")
    response = await UserRepository.get_user_by_phone(user.phone_number)
    if response:
        raise Exception("Phone number already exists.")
    response = await UserRepository.create_user(user)
    
    await publish_event(
        "USER_REGISTERED",
        {
            "email":DataBaseUser.email,
            "name":DataBaseUser.username
        }
    )
    
    access_token = create_access_token(
        {
            "sub":response.id,
            "email":str(response.email)
        }
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
    


    

    