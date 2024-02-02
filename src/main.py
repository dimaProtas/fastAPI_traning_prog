from fastapi import FastAPI
from src.auth.base_conf import auth_backend, fastapi_users
from src.auth.scemas import UserRead, UserCreate
from src.cars.router import router
from src.tasks.router import router as celery_router

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis


app = FastAPI(
    title='Cars App'
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router)
app.include_router(celery_router)


# Функция для кеширования
@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
