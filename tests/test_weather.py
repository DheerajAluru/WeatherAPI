import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_weather_unauthenticated():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/weather?city=hyderabad")
        assert response.status_code == 200
        data = response.json()
        assert "main" in data
