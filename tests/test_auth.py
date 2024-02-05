import pytest
from sqlalchemy import insert, select

from conftest import async_session_maker, client
from src.auth.models import role


async def test_add_role():
    async with async_session_maker() as session:
        stmt = insert(role).values(id=1, name="admin", permissions=None)
        await session.execute(stmt)
        await session.commit()

        query = select(role)
        result = await session.execute(query)
        assert result.all() == [(1, 'admin', None)], "Роль не добавилась"


def test_register():
    response = client.post("/auth/register", json={
        "email": "dima_pro92@gmail.com",
        "password": "1234",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "first_name": "string",
        "last_name": "string",
        "role_id": 1
    })

    assert response.status_code == 201


def test_login():
    response = client.post('/auth/jwt/login', json={
        "grant_type": "",  # Возможно, это также должно быть заполнено
        "username": "dima_pro92@gmail.com",
        "password": "1234",
        "scope": "",
        "client_id": "",
        "client_secret": ""
    })

    assert response.status_code == 200
