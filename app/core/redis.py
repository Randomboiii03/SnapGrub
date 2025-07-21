# app/core/redis.py
import redis.asyncio as redis
from fastapi import FastAPI
from .config import get_settings

settings = get_settings()

redis_client: redis.Redis = None

def init_redis(app: FastAPI):
    global redis_client
    redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)

def get_redis() -> redis.Redis:
    return redis_client
