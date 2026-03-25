from pydantic import BaseModel, EmailStr
from typing import Optional


# 🔹 Base schema (shared fields)
class UserBase(BaseModel):
    name: str
    email: EmailStr


# 🔹 Request schema (for creating user)
class UserCreate(UserBase):
    password: str


# 🔹 Request schema (for updating user)
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None


# 🔹 Response schema (what API returns)
class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True