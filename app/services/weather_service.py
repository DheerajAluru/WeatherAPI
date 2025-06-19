import requests
import os
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
import httpx
import redis.asyncio as redis
from app.config import settings
import json 
import logging 

logger=logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

load_dotenv()

OPEN_WEATHER_API_KEY=os.getenv("OPEN_WEATHER_API_KEY")
redisInit= redis.from_url(settings.REDIS_URL)

async def get_latlong(city):
        geolocator = Nominatim(user_agent="my_geocoder_app")
        location = geolocator.geocode(city)
        if location:
            return location.latitude, location.longitude
        else:
            return f"Could not find coordinates for {city}."


async def get_weather(city:str):
    key=f"weather:{city}"
    cached = await redisInit.get(key)
    if cached:
        return cached.decode()
    lat,long=await get_latlong(city)
    BASE_URL=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={settings.OPEN_WEATHER_API_KEY}"
    # response = requests.request("GET", BASE_URL)
    # return response.json()
    logger.info(f"Getting Weather details of {city}")
    async with httpx.AsyncClient() as client:
         response = await client.get(BASE_URL)
    data = response.json()
    await redisInit.set(key, json.dumps(data), ex=300)
    return data

