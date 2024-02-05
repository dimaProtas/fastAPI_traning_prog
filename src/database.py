import sqlalchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.config import PGUSER, PGPASSWORD, DB_HOST, DB_PORT, DATABASE_NAME


DATABASE_URL = f"postgresql+asyncpg://{PGUSER}:{PGPASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE_NAME}"
# Base: DeclarativeMeta = declarative_base()
Base = sqlalchemy.orm.declarative_base()

metadata = MetaData()

engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
