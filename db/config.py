import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

SECRET_KEY = "c718963fc35bf5d4e7a6be6d797c31a6eda88ea904e12bf9f561401cb7044881"


def get_connect_string(env):
    adapter = env.get('DATABASE_ADAPTER', 'postgresql+asyncpg')
    username = env.get('DATABASE_USERNAME', 'postgres')
    password = env.get('DATABASE_PASSWORD', 'postgres')
    host = env.get('DATABASE_HOST', 'localhost')
    port = env.get('DATABASE_PORT', 5432)
    db_name = env.get('DATABASE_NAME', 'postgres')
    if password:
        password = f':{password}'
    connect_string = (
        f'{adapter}://{username}{password}@{host}:{port}/{db_name}'
    )
    return connect_string


connect_string = get_connect_string(os.environ)
engine = create_async_engine(connect_string)
SessionLocal = async_sessionmaker(engine)
Base = declarative_base()
db = SessionLocal()
