from fastapi import APIRouter, Depends
from services.payment.payment_service import create_order
from utils.jwt import get_current_user

router = APIRouter(
    prefix="/payment"
)


@router.post("/create/{rider_id}")
async def pay(
    rider_id: str,
    amount: float,
    current_user=Depends(get_current_user)
):
    order = await create_order(
        amount=amount,
        user_id=current_user.id,
        rider_id=rider_id
    )

    return order