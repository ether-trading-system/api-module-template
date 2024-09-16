import logging
from contextlib import asynccontextmanager

from datetime import datetime
from sqlalchemy import func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, async_scoped_session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///app.db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True, pool_pre_ping=True)
session_factory = async_sessionmaker(engine, autoflush=False, future=True)


class Base(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())


async def init_models():
    async with engine.begin() as conn:
        logging.info("Creating tables")
        await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def get_session():
    async with session_factory() as session:
        try:
            await session.begin()
            yield session
        finally:
            await session.close()
