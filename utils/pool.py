import os
import time
from psycopg2.pool import PoolError, SimpleConnectionPool
from .constants import MAX_CONNECTIONS, MIN_CONNECTIONS, TRAILS, POOL_DELAY


class DatabaseConnection:
    connection_pool = None

    def __init__(self):
        if not DatabaseConnection.connection_pool:
            DatabaseConnection.connection_pool = SimpleConnectionPool(MIN_CONNECTIONS,
                                                                      MAX_CONNECTIONS,
                                                                      user=os.getenv("POSTGRES_USER"),
                                                                      password=os.getenv("POSTGRES_PASSWORD"),
                                                                      host="db",
                                                                      port=os.getenv("PORT"),
                                                                      database=os.getenv("POSTGRES_DB"))
            self.cursor = None
            self.connection = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DatabaseConnection, cls).__new__(cls)
        return cls.instance

    def __enter__(self):
        for _ in range(TRAILS):
            try:
                self.connection = DatabaseConnection.connection_pool.getconn()
                self.connection.autocommit = False
                self.cursor = self.connection.cursor()
                return self
            except PoolError:
                time.sleep(POOL_DELAY)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
            self.cursor.close()
            DatabaseConnection.connection_pool.putconn(self.connection)
        else:
            self.connection.commit()
            self.cursor.close()
            DatabaseConnection.connection_pool.putconn(self.connection)


pool_manager = DatabaseConnection()
