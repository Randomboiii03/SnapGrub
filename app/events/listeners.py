import asyncio
from app.core.redis import get_redis

async def handle_order_message(message: dict):
    print(f"📦 New order: {message['data']}")

async def start_redis_listeners():
    redis = get_redis()
    pubsub = redis.pubsub()
    await pubsub.subscribe("orders:global")

    print("🔊 Redis PubSub Listener started...")

    async def listen():
        async for message in pubsub.listen():
            if message["type"] == "message":
                await handle_order_message(message)

    asyncio.create_task(listen())
