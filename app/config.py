import os 
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("MONGODB_URI")
    SECRET_KEY = os. getenv("SECRET_KEY", "custom_secret_key")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
    REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

settings=Settings()