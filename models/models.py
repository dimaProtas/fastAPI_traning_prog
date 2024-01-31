from datetime import datetime

from sqlalchemy import MetaData, Integer, TIMESTAMP, ForeignKey, Table, Column, String, JSON

metadata = MetaData()

roles = Table(
    'roles',
    metadata,
    Column('id', Integer, unique=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON)
)

user = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String, nullable=False),
    Column('last_name', String),
    Column('email', String, nullable=False),
    Column('Password', String, nullable=False),
    Column('registration_at', TIMESTAMP, default=datetime.utcnow),
    Column('roles_id', Integer, ForeignKey('roles.id')),
)


# Команда "alembic init migrations" для инициализации мигрций
# Команда создающая миграции '''alembic revision --autogenerate -m "Database Created"'''
# Команда выполнения миграций '''alembic upgrade <версия миграции>'''