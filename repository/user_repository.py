from models.user import DataBaseUser
from services.database import supabase
from supabase import Client
from dataclasses import asdict
from pydantic import EmailStr

class UserRepository:
    def __init__(self,client:Client = supabase):
        self.client = client
    
    async def create_user(self,user:DataBaseUser):
        data = asdict(user)
        data.pop("id", None)
        
        response = (
            self.client
            .table("db_users")
            .insert(data)
            .execute()
        )
        if not response.data:
            return None
        return DataBaseUser(**response.data[0])
    
    async def get_user_by_email(self,email:EmailStr):
        
        response = (
            self.client
            .table("db_users")
            .select("*")
            .eq("email",email)
            .limit(1)
            .execute()
        )
        
        if not response.data:
            return None
        return DataBaseUser(**response.data[0])
    
    async def get_user_by_phone(self,phone_numner:str):
        
        response = (
            self.client
            .table("db_users")
            .select("*")
            .eq("phone_number",phone_numner)
            .limit(1)
            .execute()
        )
        
        if not response.data:
            return None
        return DataBaseUser(**response.data[0])
        
        
    