from os import environ
from loguru import logger

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

DB_URL = f"postgresql+asyncpg://{environ['FASTAPI_DB_USER']}:{environ['FASTAPI_DB_PASSWORD']}@{environ['FASTAPI_DB_HOST']}:{environ['FASTAPI_DB_PORT']}/{environ['FASTAPI_DB_NAME']}"

async_engine = create_async_engine(DB_URL, echo=True, pool_pre_ping=True)

AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=async_engine, future=True,
                                       expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


Base = declarative_base()
