from utils.distance import distance
from models.user import Driver,User

MAX_DISTANCE = 5  



def find_nearest(drivers:list[Driver],user:User):
    nearest = None
    nearest_distance = float("inf")
    for driver in drivers:

        if not driver.available:
            continue

        d = distance(
            user.latitude,
            user.longitude,
            driver.latitude,
            driver.longitude,
        )

        if d <= MAX_DISTANCE and d < nearest_distance:
            nearest = driver
            nearest_distance = d

        print(nearest)