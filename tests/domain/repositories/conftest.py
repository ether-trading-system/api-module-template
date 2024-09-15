import pytest

from packaging.metadata import Metadata
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from core import Base

async_engine: AsyncEngine = create_async_engine('sqlite+aiosqlite:///test.db', echo=True)
meta = Metadata()


@pytest.fixture(scope='function')
async def async_session():
    async with async_engine.connect() as conn:
        transaction = await conn.begin()
        await conn.run_sync(Base.metadata.create_all)

        async_session = async_sessionmaker(bind=conn, autoflush=False, autocommit=False, expire_on_commit=False)

        async with async_session() as session:
            await session.begin()
            yield session
            await session.close()
            await transaction.rollback()
