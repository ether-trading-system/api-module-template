from datetime import datetime
from sqlalchemy import MetaData, func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///app.db"

meta = MetaData()
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(meta.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
