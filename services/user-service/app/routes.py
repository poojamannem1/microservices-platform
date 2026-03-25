from fastapi import APIRouter
from app.schemas import UserCreate, UserResponse

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    return {
        "id": 1,
        "name": user.name,
        "email": user.email
    }