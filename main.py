from datetime import datetime
from enum import Enum
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse


app = FastAPI(
    title='Trading App'
)

# Валидация отправляемых данных на клиент
@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


users = [
    {'id': 1, 'name': 'Alex', 'degree': [{'id': 1, 'role': 'admin', 'created_at': '2024-01-31 12:07:35.353235'}]},
    {'id': 2, 'name': 'Jon'},
    {'id': 3, 'name': 'Ben'},
]


class RoleType(Enum):
    admin = 'admin'
    moderator = 'moderator'
    user = 'user'


class Degree(BaseModel):
    id: int
    role: RoleType
    created_at: datetime


class User(BaseModel):
    id: int
    name: str
    degree: Optional[list[Degree]] = []

# response_model используеться для валидации данных отправляемых на клиент
@app.get('/get_user/{user_id}', response_model=list[User])
def get_user(user_id: int):
    return [user for user in users if user.get('id') == user_id]



cars = [
    {'id': 1, 'car': 'Mersedes', 'model': 's-class', 'price': 10000000},
    {'id': 2, 'car': 'Audi', 'model': 'A8', 'price': 2500000},
    {'id': 3, 'car': 'BMW', 'model': 'M5', 'price': 5000000},
    {'id': 4, 'car': 'Volkswagen', 'model': 'Golf', 'price': 1500000},
    {'id': 5, 'car': 'Kia', 'model': 'Rio', 'price': 1000000},
    {'id': 6, 'car': 'Hundai', 'model': 'Solaris', 'price': 900000},
    {'id': 7, 'car': 'Toyota', 'model': 'Land Cruser', 'price': 3500000},
]

@app.get('/car')
def get_car(ofset: int = 0, limit: int = 5):
    return cars[ofset:][:limit]


@app.post('/change')
def change_name(user_id: int, name: str):
    current_user = list(filter(lambda user: user.get('id') == user_id, users))[0]
    current_user['name'] = name
    return {'status': 200, 'data': current_user}


class Car(BaseModel):
    id: int
    car: str = Field(max_length=10)
    model: str
    prise: int = Field(ge=0)


@app.post('/add_car')
def add_car(car: list[Car]):
    cars.extend(car)
    return {'status': 200, 'data': car}
