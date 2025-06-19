from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.models import ErrorResponse

class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, redis, limit: int, window: int):
        super().__init__(app)
        self.redis = redis
        self.limit = limit
        self.window = window

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        key = f"rate_limit:{client_ip}"
        count = await self.redis.incr(key)
        if count == 1:
            await self.redis.expire(key, self.window)
        if count > self.limit:
            return JSONResponse(
                status_code=429,
                content=ErrorResponse(detail="Rate limit exceeded").dict()
            )
        response = await call_next(request)
        return response
