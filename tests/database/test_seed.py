import pytest
import os

from core import Base
from core.db.seed import is_database_empty
from tests.database.conftest import async_engine


@pytest.mark.asyncio
async def test_is_database_empty():
    """Test checking if the database is empty."""

    # Remove the database file before running the test
    if os.path.exists('test.db'):
        os.remove('test.db')

    assert await is_database_empty(async_engine) is True


@pytest.mark.asyncio
async def test_is_database_not_empty():
    """Test checking if the database is not empty."""
    async with async_engine.connect() as conn:
        await conn.begin()
        await conn.run_sync(Base.metadata.create_all)

    assert await is_database_empty(async_engine) is False
