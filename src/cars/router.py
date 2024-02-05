import time

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import user
from src.cars.models import cars
from src.cars.shemas import CarCreate
from src.database import get_async_session

from fastapi_cache.decorator import cache


router = APIRouter(
    prefix='/cars',
    tags=['Cars']
)


@router.get('/get_cars')
# @cache(30)
async def get_cars(ofset: int = 0, limit: int = 2, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(cars).limit(limit).offset(ofset)
        result = await session.execute(query)
        # x = 1 / 0 # Для проверки кеширования
        # time.sleep(2)  # Для проверки кеширования
        return result.mappings().all()
    # Отлавливаем ошибку деление на 0, и возвращаем status_code=200 (так можно любые ошибки отлавливать и возвращать любой ответ и статус)
    except ZeroDivisionError:
        raise HTTPException(status_code=200, detail={
            'status': 'error',
            'data': None
        })


@router.get('/get_cars_brand')
async def get_cars_brand(brand_car: str, limit: int = 10, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(cars).where(cars.c.brand == brand_car).limit(limit)
        result = await session.execute(query)
        return result.mappings().all()
    except Exception:
        return {
            'status': 'error'
        }


@router.post('/add_car')
async def add_car(new_car: CarCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        statement = insert(cars).values(**new_car.dict())
        await session.execute(statement)
        await session.commit()
        return {'status': 'OK', 'data': new_car}
    except Exception:
        return {
            'status': 'error'
        }