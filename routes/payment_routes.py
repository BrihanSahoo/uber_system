from fastapi import APIRouter
from services.payment.payment_service import create_order,verify_payment


router = APIRouter(
    prefix="/payment"
)


@router.post("/create/{user_id}/{rider_id}")
async def pay(amount:float,user_id:str,rider_id:str):
    order = await create_order(amount)

