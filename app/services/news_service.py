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
    # response=requests.get(BASE_URL,params=params)
    # return response.json()
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
    data = response.json()
    logger.info(f"Data: {data}")
    await redisInit.set(key, json.dumps(data), ex=300)
    return data

# import requests
# BASE_URL = "https://newsapi.org/v2/top-headlines"
# params = {"q": "india","apikey": NEWS_API_KEY }
# topic ="Hyderabad weather"
# #BASE_URL_everything=f"https://newsapi.org/v2/everything?q={topic}&from=2025-05-17&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
# BASE_URL_Headlines=f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={NEWS_API_KEY}"

# response=requests.get(BASE_URL,params=params)

# print(response.json())

"""
https://openweathermap.org/api
https://openweathermap.org/api/one-call-3#concept

https://newsapi.org/
https://newsapi.org/docs/client-libraries/python
https://newsapi.org/docs/endpoints/top-headlines


"""