import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_signup_login_logout():
    async with AsyncClient(app=app, base_url="http://test") as client:
        #  Signup
        response = await client.post("/signup", json={
            "name": "testuser",
            "email": "test@example.com",
            "password": "testpassword"
        })
        assert response.status_code in [200, 400]  # Allow 400 if user already exists

        #  Login
        response = await client.post("/login", data={
            "username": "test@example.com",
            "password": "testpassword"
        })
        assert response.status_code == 200
        data = response.json()
        token = data.get("access_token")
        assert token

        headers = {"Authorization": f"Bearer {token}"}

        # Test authenticated endpoint before logout
        response = await client.get("/news?search=india", headers=headers)
        assert response.status_code == 200

        # Logout
        response = await client.post("/logout", headers=headers)
        assert response.status_code == 200
        assert response.json()["data"]["message"] == "Logged out successfully"

        #  Access after logout - token should now be invalid
        response = await client.get("/news?search=india", headers=headers)
        assert response.status_code == 401  # Unauthorized
