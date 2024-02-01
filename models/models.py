from datetime import datetime

from sqlalchemy import MetaData, Integer, TIMESTAMP, ForeignKey, Table, Column, String, JSON, Boolean

metadata = MetaData()

role = Table(
    'role',
    metadata,
    Column('id', Integer, unique=True, primary_key=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON)
)

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String, nullable=False),
    Column('last_name', String),
    Column('email', String, nullable=False),
    Column('hashed_password', String, nullable=False),
    Column('registration_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey(role.c.id)),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
)


# Команда "alembic init migrations" для инициализации мигрций
# Команда создающая миграции '''alembic revision --autogenerate -m "Database Created"'''
# Команда выполнения миграций '''alembic upgrade <версия миграции>''' используй 'head' для обновления до последней версии