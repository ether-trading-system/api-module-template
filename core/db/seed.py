from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import AsyncEngine
from core import get_session, engine, init_models
from core.db.seed_data import wine_data
from domain.wine.entities import Wine, Rating


async def is_database_empty(engine: AsyncEngine) -> bool:
    async with engine.connect() as conn:
        tables = await conn.run_sync(
            lambda con: inspect(con).get_table_names()
        )

    return not tables


async def seed_database():
    async with get_session() as session:
        wines = [*map(lambda wine: Wine(
            winery=wine['winery'],
            wine=wine['wine'],
            rating=Rating(
                average=wine['rating']['average'],
                reviews=wine['rating']['reviews']
            ),
            location=wine['location'],
            image=wine['image']
        ), wine_data)]

        print(wines)
        session.add_all(wines)
        await session.commit()
