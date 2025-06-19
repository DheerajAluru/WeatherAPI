from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime,timezone
from app.schema import UserCreate, UserLogin, Token
from app.utils import get_password_hash, verify_password, blacklist_token, create_access_token
from app.models import User, SuccessResponse
from app.auth import get_current_user, oauth2_scheme
from jose import jwt 
from app.config import settings


router = APIRouter()

@router.post("/signup")
async def signup(user: UserCreate):
    existing_user = await User.find_one(User.email == user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already Exists")
    password = get_password_hash(user.password)
    new_user = User(name=user.name, email= user.email, password=password)
    await new_user.insert()
    return {"message": "User created successfully"}

@router.post("/signin", response_model=Token)
async def signin(user: UserLogin):
    existing_user = await User.find_one(User.email == user.email)
    if not existing_user or not verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token({"sub": existing_user.email})
    return {"access_token": access_token}

@router.post("/logout")
async def logout(current_user: User = Depends(get_current_user), token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    exp = payload.get("exp")
    expires_in = exp - int(datetime.now().timestamp())
    if expires_in < 0:
        expires_in = 0
    await blacklist_token(token, expires_in)
    return SuccessResponse(data={"message": "Logged out successfully"})

