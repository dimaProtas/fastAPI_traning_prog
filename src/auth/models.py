from datetime import datetime
from typing import Union
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, TIMESTAMP, ForeignKey, Table, Column, String, JSON, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base, metadata


role = Table(
    'role',
    metadata,
    Column('id', Integer, unique=True, primary_key=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON)
)

# user = Table(
#     'user',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('first_name', String, nullable=False),
#     Column('last_name', String),
#     Column('email', String, nullable=False),
#     Column('hashed_password', String, nullable=False),
#     Column('registration_at', TIMESTAMP, default=datetime.utcnow),
#     Column('role_id', Integer, ForeignKey(role.c.id)),
#     Column('is_active', Boolean, default=True, nullable=False),
#     Column('is_superuser', Boolean, default=False, nullable=False),
#     Column('is_verified', Boolean, default=False, nullable=False),
# )


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(length=100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(length=100))
    registration_at: Mapped[Union[datetime, None]] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey(role.c.id))
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)



