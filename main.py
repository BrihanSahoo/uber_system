from fastapi import FastAPI

from services.driver_service import find_driver
from routes.payment_routes import router as payment_router


app = FastAPI()



app.include_router(payment_router)


@app.get("/health")
def root():
    return {
        "message":"working"
    }