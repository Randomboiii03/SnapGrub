from app.core.redis import get_redis

async def publish_order(tenant_id: str, data: dict):
    redis = get_redis()
    await redis.publish(f"orders:{tenant_id}", str(data))
