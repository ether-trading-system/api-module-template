from fastapi import APIRouter

router = APIRouter(prefix="/wines", tags=["wines"])


@router.get("")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]