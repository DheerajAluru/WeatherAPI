import requests
import os
import httpx
import redis.asyncio as redis
from app.config import settings
import json
from dotenv import load_dotenv
import logging 

logger=logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
load_dotenv()

redisInit= redis.from_url(settings.REDIS_URL)

NEWS_API_KEY=os.getenv("NEWS_API_KEY")

async def get_news(query: str | None = None ):
    key=f"news:{query or 'top-headllines'}"
    cached = await redisInit.get(key)
    if cached:
        return cached.decode()
    BASE_URL = "https://newsapi.org/v2/top-headlines"
    params = {"q": query, "apikey": NEWS_API_KEY }
    if query:
        params["q"] = query
    logger.info(f"Getting Headlines about {query}")
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
    data = response.json()
    logger.info(f"Data: {data}")
    await redisInit.set(key, json.dumps(data), ex=300)
    return data
