from fastapi import FastAPI
from src.auth.base_conf import auth_backend, fastapi_users
from src.auth.scemas import UserRead, UserCreate
from src.cars.router import router


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