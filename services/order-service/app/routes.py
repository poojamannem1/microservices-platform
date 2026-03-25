from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# 🔹 Fake DB (replace later with PostgreSQL)
orders_db = []


# 🔹 Schema
class Order(BaseModel):
    id: int
    user_id: int
    product_name: str
    quantity: int


# 🔹 Create Order
@router.post("/", response_model=Order)
def create_order(order: Order):
    orders_db.append(order)
    return order


# 🔹 Get All Orders
@router.get("/", response_model=List[Order])
def get_orders():
    return orders_db


# 🔹 Get Order by ID
@router.get("/{order_id}", response_model=Order)
def get_order(order_id: int):
    for order in orders_db:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")