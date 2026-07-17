from services.database import supabase

def add_driver(
    name,
    latitude,
    longitude
):

    query = f"""
    INSERT INTO drivers
    (
        name,
        location
    )

    VALUES

    (
        '{name}',

        ST_SetSRID(
            ST_MakePoint(
                {longitude},
                {latitude}
            ),
            4326
        )
    );
    """

    return query

def create_driver(
    name,
    lat,
    lon
):

    response = supabase.rpc(
        "add_driver",
        {
            "driver_name":name,
            "lat":lat,
            "lon":lon
        }
    ).execute()


    return response


def find_driver(
    lat,
    lon
):

    result = supabase.rpc(
        "find_nearest_driver",
        {
            "user_lat":lat,
            "user_lon":lon,
            "radius":5000
        }

    ).execute()


    return result.data