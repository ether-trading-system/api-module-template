from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core import get_session
from domain.wine.wine_service import WineService

router = APIRouter(prefix="/wines", tags=["wines"])


@router.get("")
async def get_wines(
        session: AsyncSession = Depends(get_session)
):
    _service = WineService(session)
    return await _service.get_all_wines()


@router.get("")
async def get_wine():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.post("", status_code=201)
async def create_wine():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.put("")
async def update_wine():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.delete("", status_code=204)
async def delete_wine():
    return [{"username": "Rick"}, {"username": "Morty"}]
