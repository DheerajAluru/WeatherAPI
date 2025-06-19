from pydantic import EmailStr, BaseModel
from beanie import Document
from typing import Any, Optional


class User(Document):
    name : str 
    email : EmailStr 
    password : str

    class Settings:
        name = "users"


class SuccessResponse(BaseModel):
    status: str = "success"
    data: Any

class ErrorResponse(BaseModel):
    status: str = "error"
    detail: Optional[str] = None