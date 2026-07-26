from fastapi import APIRouter
from services.user.login_service import login
from services.user.register_service import register
from pydantic import EmailStr
from models.user import DataBaseUser

router = APIRouter(
    prefix="/user"
)


@router.post("/register")
async def register_user(
    username:str,
    email:EmailStr,
    password:str,
    phone_number:str
):
    user = DataBaseUser(
        username=username,
        email=email,
        hashed_password=password,
        phone_number=phone_number
    )
    
    response = await register(user)
    
    return response

@router.post("/login")
async def login_user(
    email:EmailStr,
    password:str
):
    response = await login(email,password)
    
    return response