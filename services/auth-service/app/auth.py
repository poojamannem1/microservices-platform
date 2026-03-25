from fastapi import APIRouter, HTTPException
from app.schemas import LoginRequest

router = APIRouter()

@router.post("/login")
def login(data: LoginRequest):
    if data.email == "test@test.com" and data.password == "1234":
        return {"message": "Login successful"}

    raise HTTPException(status_code=401, detail="Invalid credentials")