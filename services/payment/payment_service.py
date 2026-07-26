from fastapi import HTTPException
import razorpay
from config import settings
from schemas.verify_payments import VerifyPayment

client = razorpay.Client(
    auth=(settings.RAZOR_ID,settings.RAZOR_SECRET)
)


async def create_order(amount):

    data = {
        "amount":amount,   
        "currency": "INR",
        "receipt": "receipt_001",
        "payment_capture": 1
    }

    order = client.order.create(data=data)

    return order

async def verify_payment(data:VerifyPayment):
    params = {
        "razorpay_order_id": data.razorpay_order_id,
        "razorpay_payment_id": data.razorpay_payment_id,
        "razorpay_signature": data.razorpay_signature,
    }
    try:
        client.utility.verify_payment_signature(params)
        return {
            "success": True,
            "message": "Payment verified"
        }

    except razorpay.errors.SignatureVerificationError:
        raise HTTPException(
            status_code=400,
            detail="Invalid signature"
        )