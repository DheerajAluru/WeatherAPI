import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_news_authenticated():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Login first to get token
        response = await client.post("/login", data={
            "username": "test@example.com",
            "password": "testpassword"
        })
        token = response.json().get("access_token")
        headers = {"Authorization": f"Bearer {token}"}

        # Now hit /news endpoint
        response = await client.get("/news?search=india", headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert "articles" in data
