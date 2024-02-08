from sqlalchemy import Integer, TIMESTAMP, ForeignKey, Table, Column, String, JSON, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.auth.models import User
from src.database import metadata, Base

cars = Table(
    'cars',
    metadata,
    Column('id', Integer, primary_key=True, unique=True, autoincrement=True),
    Column('brand', String(length=100), nullable=False),
    Column('model', String(length=100), nullable=False),
    Column('price', Integer),
    Column('color', String(length=50), nullable=False),
    Column('user_id', Integer, ForeignKey(User.id))
)
