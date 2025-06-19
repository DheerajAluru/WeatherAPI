from fastapi import FastAPI,Request, HTTPException
from app.database import init_db
from app.routes import *
from contextlib import asynccontextmanager
from app.routes import news,users,weather
from app.models import SuccessResponse, ErrorResponse
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.middleware import RateLimiterMiddleware
from app.utils import redisInit

import logging 
logger=logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan= lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(
    RateLimiterMiddleware,
    redis=redisInit,
    limit=10,      # 10 requests
    window=60      # per 60 seconds
)
#include routes

app.include_router(users.router)
app.include_router(news.router)
app.include_router(weather.router)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(detail=str(exc)).model_dump()
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(detail=exc.detail).model_dump()
    )