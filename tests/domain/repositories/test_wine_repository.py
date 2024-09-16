import pytest
import logging

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from domain.wine.entities.rating import Rating
from domain.wine.entities.wine import Wine
from domain.wine.wine_repository import WineRepository


@pytest.fixture(scope='function')
async def wine_repository(async_session: AsyncSession):
    yield WineRepository(async_session)


@pytest.fixture(scope='function', autouse=True)
async def clear_wines(async_session: AsyncSession):
    logging.info('Tearing down wine repo')
    await async_session.execute(delete(Wine))
    await async_session.execute(delete(Rating))
    await async_session.commit()
    yield


@pytest.mark.asyncio
async def test_create_wine(wine_repository: WineRepository):
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
    saved_wine = await wine_repository.save(wine)

    assert saved_wine.id is not None


@pytest.mark.asyncio
async def test_update_wine(wine_repository: WineRepository):
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
    saved_wine = await wine_repository.save(wine)

    saved_wine.winery = 'Maselva 2'
    updated_wine = await wine_repository.save(saved_wine)

    assert updated_wine.winery == 'Maselva 2'


@pytest.mark.asyncio
async def test_find_all_wines(wine_repository: WineRepository):
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
    await wine_repository.save(wine)

    wines = await wine_repository.find_all()

    assert len(wines) == 1
    assert wines[0].winery == 'Maselva'
    assert wines[0].wine == 'Emporda 2012'
    assert wines[0].rating.average == 4.9
    assert wines[0].rating.reviews == 88
    assert wines[0].location == 'Spain\n·\nEmpordà'
    assert wines[0].image == 'https://images.vivino.com/thumbs/ApnIiXjcT5Kc33OHgNb9dA_375x500.jpg'


@pytest.mark.asyncio
async def test_find_by_id_wine(wine_repository: WineRepository):
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
    saved_wine = await wine_repository.save(wine)
    found_wine = await wine_repository.find_by_id(saved_wine.id)

    assert found_wine == saved_wine


@pytest.mark.asyncio
async def test_delete_wine(wine_repository: WineRepository):
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
    saved_wine = await wine_repository.save(wine)
    await wine_repository.delete(saved_wine)

    wines = await wine_repository.find_all()

    assert len(wines) == 0
