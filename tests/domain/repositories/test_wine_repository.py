import pytest
import logging

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from domain.wine.models.rating import Rating
from domain.wine.models.wine import Wine
from domain.wine.wine_repository import WineRepository


@pytest.fixture(scope='function', autouse=True)
async def teardown_wine_repo(async_session: AsyncSession):
    yield
    logging.info('Tearing down wine repo')
    await async_session.execute(delete(Wine))
    await async_session.execute(delete(Rating))
    await async_session.commit()


@pytest.mark.asyncio
async def test_create_wine(async_session: AsyncSession):
    """Test creating a wine in the database."""
    wine = Wine(
        winery='Maselva',
        wine='Emporda 2012',
        rating=Rating(
            average=4.9,
            reviews=88
        ),
        location='Spain\n·\nEmpordà',
        image='https://images.vivino.com/thumbs/ApnIiXjcT5Kc33OHgNb9dA_375x500.jpg'
    )
    wine_repo = WineRepository(async_session)
    saved_wine = await wine_repo.save(wine)

    assert saved_wine.id is not None


@pytest.mark.asyncio
async def test_update_wine(async_session: AsyncSession):
    """Test updating a wine in the database."""
    wine = Wine(
        winery='Maselva',
        wine='Emporda 2012',
        rating=Rating(
            average=4.9,
            reviews=88
        ),
        location='Spain\n·\nEmpordà',
        image='https://images.vivino.com/thumbs/ApnIiXjcT5Kc33OHgNb9dA_375x500.jpg'
    )
    wine_repo = WineRepository(async_session)
    saved_wine = await wine_repo.save(wine)

    saved_wine.winery = 'Maselva 2'
    updated_wine = await wine_repo.save(saved_wine)

    assert updated_wine.winery == 'Maselva 2'


@pytest.mark.asyncio
async def test_find_all_wines(async_session: AsyncSession):
    """Test finding all wines in the database."""
    wine = Wine(
        winery='Maselva',
        wine='Emporda 2012',
        rating=Rating(
            average=4.9,
            reviews=88
        ),
        location='Spain\n·\nEmpordà',
        image='https://images.vivino.com/thumbs/ApnIiXjcT5Kc33OHgNb9dA_375x500.jpg'
    )
    wine_repo = WineRepository(async_session)
    await wine_repo.save(wine)

    wines = await wine_repo.find_all()

    assert len(wines) == 1
    assert wines[0].winery == 'Maselva'
    assert wines[0].wine == 'Emporda 2012'
    assert wines[0].rating.average == 4.9
    assert wines[0].rating.reviews == 88
    assert wines[0].location == 'Spain\n·\nEmpordà'
    assert wines[0].image == 'https://images.vivino.com/thumbs/ApnIiXjcT5Kc33OHgNb9dA_375x500.jpg'


@pytest.mark.asyncio
async def test_find_by_id_wine(async_session: AsyncSession):
    """Test finding a wine by its ID in the database."""
    wine = Wine(
        winery='Maselva',
        wine='Emporda 2012',
        rating=Rating(
            average=4.9,
            reviews=88
        ),
        location='Spain\n·\nEmpordà',
        image='https://images.vivino.com/thumbs/ApnIiXjcT5Kc33OHgNb9dA_375x500.jpg'
    )
    wine_repo = WineRepository(async_session)
    saved_wine = await wine_repo.save(wine)
    found_wine = await wine_repo.find_by_id(saved_wine.id)

    assert found_wine == saved_wine


@pytest.mark.asyncio
async def test_delete_wine(async_session: AsyncSession):
    """Test deleting a wine from the database."""
    wine = Wine(
        winery='Maselva',
        wine='Emporda 2012',
        rating=Rating(
            average=4.9,
            reviews=88
        ),
        location='Spain\n·\nEmpordà',
        image='https://images.vivino.com/thumbs/ApnIiXjcT5Kc33OHgNb9dA_375x500.jpg'
    )
    wine_repo = WineRepository(async_session)
    saved_wine = await wine_repo.save(wine)
    await wine_repo.delete(saved_wine)

    wines = await wine_repo.find_all()

    assert len(wines) == 0
