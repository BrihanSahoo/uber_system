import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    RAZOR_ID = os.getenv("RAZOR_ID")
    RAZOR_SECRET = os.getenv("RAZOR_SECRET")
    EMAIL = os.getenv("EMAIL")
    EMAIL_PASS = os.getenv("EMAIL_PASS")
    COMPANY_NAME = os.getenv("COMPANY_NAME")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    REDIS_URL = os.getenv("REDIS_URL")

settings = Settings()