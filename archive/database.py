import time
import psycopg2
from psycopg2.extras import RealDictCursor
from app.config import Settings


def create_connection():
    app_settings = Settings()
    while True:
        try:
            conn = psycopg2.connect(
                host=app_settings.db_host,
                port=app_settings.db_port,
                dbname=app_settings.db_name,
                user=app_settings.db_username,
                password=app_settings.db_password,
                cursor_factory=RealDictCursor,  # this lib doesnt return the column name,
                # cursor_factory is commonly used for RealDictCursor to get results as dictionaries.
            )
            cursor = conn.cursor()
            print("Database connection was successful")
            return conn, cursor
        except Exception as error:
            print("Things failed, retry")
            print(f"Error: {error}")
            time.sleep(2)
