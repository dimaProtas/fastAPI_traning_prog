from dotenv import load_dotenv
import os


load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
PGUSER = os.environ.get("PGUSER")
PGPASSWORD = os.environ.get("PGPASSWORD")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
SECRET_AUTH = os.environ.get("SECRET_AUTH")

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")

GMAIL_USER = os.environ.get("GMAIL_USER")
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")


DB_HOST_TEST = os.environ.get("DB_HOST_TEST")
DB_PORT_TEST = os.environ.get("DB_PORT_TEST")
PGUSER_TEST = os.environ.get("PGUSER_TEST")
PGPASSWORD_TEST = os.environ.get("PGPASSWORD_TEST")
DATABASE_NAME_TEST = os.environ.get("DATABASE_NAME_TEST")