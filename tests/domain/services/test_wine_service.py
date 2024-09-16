import pytest
import logging

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from domain.wine.models import Wine, Rating
from domain.wine.schemas import WineCreate, RatingCreate, WineUpdate, RatingUpdate
from domain.wine.wine_service import WineService


@pytest.fixture(scope='function')
async def wine_service(async_session: AsyncSession):
    yield WineService(async_session)


@pytest.fixture(scope='function', autouse=True)
async def clear_wines(async_session: AsyncSession):
    logging.info('Tearing down wine repo')
    await async_session.execute(delete(Wine))
    await async_session.execute(delete(Rating))
    await async_session.commit()
    yield


wine_mock = {
    'winery': 'Maselva',
    'wine': 'Emporda 2012',
    'rating': {
        'average': 4.9,
        'reviews': 88
    },
    'location': 'Spain\n·\nEmpordà',
    'image': 'https://images.vivino.com/thumbs/ApnIiXjcT5Kc33OHgNb9dA_375x500.jpg'
}


@pytest.mark.asyncio
async def test_create_wine(wine_service: WineService):
    """Test creating a wine in the database."""
    wine: WineCreate = WineCreate(
        winery='Maselva',
        wine='Emporda 2012',
        rating=RatingCreate(
            average=4.9,
            reviews=88
        ),
        location='Spain\n·\nEmpordà',
        image='https://images.vivino.com/thumbs/ApnIiXjcT5Kc33OHgNb9dA_375x500.jpg'
    )
    saved_wine = await wine_service.create_wine(wine)

    assert saved_wine.id is not None


@pytest.mark.asyncio
async def test_get_all_wines(wine_service: WineService):
    """Test getting all wines from the database."""
    wine: WineCreate = WineCreate(
        winery='Maselva',
        wine='Emporda 2012',
        rating=RatingCreate(
            average=4.9,
            reviews=88
        ),
        location='Spain\n·\nEmpordà',
        image='https://images.vivino.com/thumbs/ApnIiXjcT5Kc33OHgNb9dA_375x500.jpg'
    )
    await wine_service.create_wine(wine)
    wines = await wine_service.get_all_wines()

    assert len(wines) == 1


@pytest.mark.asyncio
async def test_get_wine_by_id(wine_service: WineService):
    """Test getting a wine by its ID."""
    wine: WineCreate = WineCreate(
        winery='Maselva',
        wine='Emporda 2012',
        rating=RatingCreate(
            average=4.9,
            reviews=88
        ),
        location='Spain\n·\nEmpordà',
        image='https://images.vivino.com/thumbs/ApnIiXjcT5Kc33OHgNb9dA_375x500.jpg'
    )
    saved_wine: Wine = await wine_service.create_wine(wine)
    get_wine = await wine_service.get_wine_by_id(saved_wine.id)

    assert get_wine is not None


@pytest.mark.asyncio
async def test_update_wine(wine_service: WineService):
    """Test updating a wine in the database."""
    wine: WineCreate = WineCreate(
        winery='Maselva',
        wine='Emporda 2012',
        rating=RatingCreate(
            average=4.9,
            reviews=88
        ),
        location='Spain\n·\nEmpordà',
        image='https://images.vivino.com/thumbs/ApnIiXjcT5Kc33OHgNb9dA_375x500.jpg'
    )
    saved_wine = await wine_service.create_wine(wine)
    updated_wine = await wine_service.update_wine(WineUpdate(
        id=saved_wine.id,
        winery='Maselva',
        wine='Emporda 2012',
        rating=RatingUpdate(
            average=4.9,
            reviews=88
        ),
        location='Spain\n·\nEmpordà',
        image='https://images.vivino.com/thumbs/ApnIiXjcT5Kc33OHgNb9dA_375'
    ))

    assert updated_wine.id is not None


@pytest.mark.asyncio
async def test_delete_wine(wine_service: WineService):
    """Test deleting a wine from the database."""
    wine: WineCreate = WineCreate(
        winery='Maselva',
        wine='Emporda 2012',
        rating=RatingCreate(
            average=4.9,
            reviews=88
        ),
        location='Spain\n·\nEmpordà',
        image='https://images.vivino.com/thumbs/ApnIiXjcT5Kc33OHgNb9dA_375x500.jpg'
    )
    saved_wine = await wine_service.create_wine(wine)
    deleted_wine = await wine_service.delete_wine(saved_wine.id)

    assert deleted_wine is True
