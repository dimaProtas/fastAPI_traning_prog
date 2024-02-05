# from tests.conftest import client
from httpx import AsyncClient


async def test_add_car(ac: AsyncClient):
    response = await ac.post('/cars/add_car', json={
        "brand": "Kia",
        "model": "k5",
        "price": 200000,
        "color": "red",
        "user_id": 1
    })

    assert response.status_code == 200


async def test_get_cars_brand(ac: AsyncClient):
    response = await ac.get("/cars/get_cars_brand", params={
        "brand_car": "Kia",
        "limit": 10,
    })

    assert response.json()[0]['brand'] == "Kia"
    assert response.status_code == 200


async def test_get_cars(ac: AsyncClient):
    response = await ac.get("/cars/get_cars", params={
        "ofset": 2,
        "limit": 2,
    })

    assert response.status_code == 200
