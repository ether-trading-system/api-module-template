from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from domain.wine.entities.wine import Wine


class WineRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, wine: Wine) -> Wine:
        if not wine.id:
            self.session.add(wine)
        # else:
        #     await self.session.execute(update(Wine).where(Wine.id == wine.id).values(wine))
        await self.session.commit()
        await self.session.refresh(wine)
        return wine

    async def find_all(self) -> list[Wine]:
        wines = await self.session.execute(select(Wine))
        return [*wines.scalars().all()]

    async def find_by_id(self, wine_id: str) -> Wine:
        wine = await self.session.execute(select(Wine).where(Wine.id == wine_id))
        return wine.scalar()

    async def delete(self, wine: Wine) -> bool:
        await self.session.execute(delete(Wine).where(Wine.id == wine.id))
        return True
