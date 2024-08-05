import time
import psycopg2
from psycopg2.extras import RealDictCursor


def create_connection():
    while True:
        try:
            conn = psycopg2.connect(
                host="localhost",
                port="5432",
                dbname="postgres",
                user="postgres",
                password="12345",
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
