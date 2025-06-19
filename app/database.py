from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models import User
from app.config import settings

async def init_db():
    client= AsyncIOMotorClient(settings.DATABASE_URL)
    db = client['news_users']
    await init_beanie(database=db,document_models=[User])
