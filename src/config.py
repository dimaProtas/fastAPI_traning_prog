from dotenv import load_dotenv
import os


load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
PGUSER = os.environ.get("PGUSER")
PGPASSWORD = os.environ.get("PGPASSWORD")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
SECRET_AUTH = os.environ.get("SECRET_AUTH")
