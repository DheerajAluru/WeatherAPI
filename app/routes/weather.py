from fastapi import APIRouter, Depends
from app.services.weather_service import get_weather
from app.models import SuccessResponse
router = APIRouter()

@router.get("/weather")
async def weatherinfo(city : str):
    weather_data = await get_weather(city)
    return SuccessResponse(data=weather_data)
