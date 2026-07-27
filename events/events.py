from message_queue.redis_client import redis_client
import json

async def publish_event(event_type,data:dict):
    
    await redis_client.xadd(
        "events",
        {
            "type":event_type,
            "data":json.dumps(data)
        }
    )