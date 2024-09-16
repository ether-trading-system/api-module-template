from sqlalchemy.ext.asyncio import AsyncSession
from .entities import Wine, Rating
from .models import WineCreate, WineUpdate
from .wine_repository import WineRepository


class WineService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.wine_repository = WineRepository(session)

    async def get_wine_by_id(self, wine_id) -> Wine:
        return await self.wine_repository.find_by_id(wine_id)

    async def get_all_wines(self) -> list[Wine]:
        return await self.wine_repository.find_all()

    async def create_wine(self, create_wine: WineCreate) -> Wine:
        await self.session.begin_nested()
        wine: Wine = Wine(
            winery=create_wine.winery,
            wine=create_wine.wine,
            rating=Rating(
                average=create_wine.rating.average,
                reviews=create_wine.rating.reviews
            ),
            location=create_wine.location,
            image=create_wine.image
        )
        return await self.wine_repository.save(wine)

    async def update_wine(self, update_wine: WineUpdate) -> Wine:
        wine = await self.wine_repository.find_by_id(update_wine.id)
        wine.winery = update_wine.winery
        wine.wine = update_wine.wine
        wine.rating.average = update_wine.rating.average
        wine.rating.reviews = update_wine.rating.reviews
        wine.location = update_wine.location
        wine.image = update_wine.image
        return await self.wine_repository.save(wine)

    async def delete_wine(self, wine_id: str) -> bool:
        await self.session.begin_nested()
        wine = await self.wine_repository.find_by_id(wine_id)
        return await self.wine_repository.delete(wine)
