from app.config import settings
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta, timezone
import redis.asyncio as redis
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expiry_timeDelta: timedelta | None = None):
    to_encode = data.copy()
    expiry = datetime.now(timezone.utc) + (expiry_timeDelta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp":expiry})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

redisInit = redis.from_url(settings.REDIS_URL)

async def blacklist_token(token: str, expires_in: int):
    await redisInit.setex(f"blacklist:{token}", expires_in, 1)

async def is_token_blacklisted(token: str) -> bool:
    return await redisInit.exists(f"blacklist:{token}") == 1