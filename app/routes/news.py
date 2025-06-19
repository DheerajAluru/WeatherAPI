from fastapi import APIRouter, Depends
from app.auth import get_current_user
from app.services.news_service import get_news
from app.models import SuccessResponse

router = APIRouter()

@router.get("/news")
async def news(query: str | None = None, user = Depends(get_current_user)):
    news_data = await get_news(query)
    return SuccessResponse(data=news_data)