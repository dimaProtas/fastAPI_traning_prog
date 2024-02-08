#!/bin/bash

# Ожидание доступности базы данных
wait-for-it -t 60 postgres:5432 -- echo "Postgres is up"

alembic upgrade head

#cd src

gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000