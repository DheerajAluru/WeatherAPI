# 📰 Weather & News API Backend (FastAPI + MongoDB + Redis + JWT)

A fully async production-ready backend API built with:

- ✅ **FastAPI**
- ✅ **MongoDB (Beanie ORM)**
- ✅ **Redis (Caching + JWT Blacklist for Logout + Rate Limiting)**
- ✅ **JWT Authentication (Login, Signup, Logout)**
- ✅ **Weather API (Unauthenticated)**
- ✅ **News API (Authenticated using NewsAPI)**
- ✅ **Custom Success & Error Response Models**
- ✅ **Centralized Exception Handling**
- ✅ **Rate Limiting Middleware**
- ✅ **Fully Dockerized (MongoDB, Redis, Backend)**
- ✅ **Fully Tested using `pytest`**

---

## 🔧 Features

- User Registration (`/signup`)
- Login with JWT (`/login`)
- Logout (Token Blacklist) (`/logout`)
- Token refresh for login
- Fetch News (requires auth) (`/news`)
- Fetch Weather (no auth) (`/weather`)
- Redis-backed caching for weather API
- Global centralized exception handling
- Clean consistent response models
- Rate limiting middleware
- Full Docker Compose for easy deployment
- Fully async using `httpx`, `redis.asyncio`, `motor`, `beanie`

---

## ⚙️ Technologies

| Tool | Purpose |
|------|---------|
| **FastAPI** | API Framework |
| **Beanie** | Async ODM for MongoDB |
| **Redis** | Caching + Token blacklist + Rate Limiting |
| **JWT** | Authentication |
| **httpx** | Async external API calls |
| **pytest** | Automated Testing |
| **Docker Compose** | Local deployment |

---

## Folder Structure

```
app/
│
├── routes/         
│   ├── news.py
│   ├── users.py
│   └── weather.py
│
├── services/       
│   ├── news_service.py
│   └── weather_service.py
│
├── auth.py
├── config.py
├── database.py
├── main.py
├── middleware.py
├── models.py
├── schema.py
├── utils.py
│
tests/
│   ├── test_auth.py
│   ├── test_news.py
│   └── test_weather.py
│
docker-compose.yml
Dockerfile
requirements.txt
.env
README.md

```

## 🚀 Quick Start

### Prerequisites
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 1️⃣ Clone repo

## .env sample 

```
OPEN_WEATHER_API_KEY=<your_WeatherAPI_key>
NEWS_API_KEY=<your_newsAPI_key>
SECRET_KEY=<your_secret>
MONGODB_URI=<your_mongodb_url> # example : localhost:27017
REDIS_URL=<your_redis_url> # example : localhost:6379/

```

```bash
git clone https://github.com/DheerajAluru/WeatherAPI.git
cd WeatherAPI
```
### 2. Run via Docker Compose
```bash
docker-compose up --build
```

- Backend API: http://localhost:8000/docs
- mongodb : http://localhost:27017

---

## 🛠 Development (Locally)

### Backend
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Screenshots

![image](https://drive.google.com/uc?export=view&id=1LK4rCzlJjPM149IylFchgxEN0l0Zxu7b)
![image](https://drive.google.com/uc?export=view&id=1G35AHLM6XQseq5F-tCl-IQX1jAg0RNhf)

## Future Improvements

- The current execution can be refactored and optimized a bit further to improve code encapsulation and optimization
- Although existing scenarios for users working as expected, we can still improve it further to enchance security
- The news and weather forecast apis can be extended  further by adding more filters for specific use cases
- More logging and validations can be implemented for proper error handling.