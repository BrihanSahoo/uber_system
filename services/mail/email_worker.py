from mail.mail_service import send_welcome_email
from message_queue.redis_client import redis_client
import asyncio
import json


async def worker():

    while True:

        messages = await redis_client.xread(
            {
                "events": "$"
            },
            block=5000
        )

        if not messages:
            continue


        for stream, events in messages:

            for event_id, data in events:


                if data["type"] == "USER_REGISTERED":

                    user_data = json.loads(
                        data["data"]
                    )

                    print(
                        "Sending email:",
                        user_data["email"]
                    )

                    try:

                        await send_welcome_email(
                            name=user_data["name"],
                            email=user_data["email"]
                        )

                        print(
                            "Email sent successfully"
                        )

                    except Exception as e:

                        print(
                            "EMAIL SEND FAILED:",
                            e
                        )


asyncio.run(worker())