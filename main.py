from fastapi import FastAPI

from services.driver_service import find_driver


app = FastAPI()



@app.get("/nearest-driver")
def nearest_driver(
    lat:float,
    lon:float
):

    driver=find_driver(
        lat,
        lon
    )


    return {
        "driver":driver
    }