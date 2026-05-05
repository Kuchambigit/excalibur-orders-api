# import router, typing, schema, and exception handling
from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.order_schema import OrderSchema

# create router instance
router = APIRouter()

# simple in-memory storage (acts like a fake database)
orders_db: List[OrderSchema] = []


# -------------------------------
# GET /orders (get all orders)
# -------------------------------
@router.get("/orders", response_model=List[OrderSchema])
def get_orders():
    return orders_db


# -------------------------------
# GET /orders/{id} (get one order)
# -------------------------------
@router.get("/orders/{order_id}", response_model=OrderSchema)
def get_order(order_id: int):
    for order in orders_db:
        if order.order_id == order_id:
            return order

    raise HTTPException(status_code=404, detail="Order not found")


# -------------------------------
# POST /orders (create order)
# -------------------------------
@router.post("/orders", response_model=OrderSchema)
def create_order(order: OrderSchema):
    orders_db.append(order)
    return order


# -------------------------------
# DELETE /orders/{id}
# -------------------------------
@router.delete("/orders/{order_id}")
def delete_order(order_id: int):
    for index, order in enumerate(orders_db):
        if order.order_id == order_id:
            deleted_order = orders_db.pop(index)

            return {
                "message": "Order deleted successfully",
                "order": deleted_order
            }

    raise HTTPException(status_code=404, detail="Order not found")
