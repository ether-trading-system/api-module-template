from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from domain.wine.models.rating_schema import RatingModel, RatingCreate, RatingUpdate


class WineBase(BaseModel):
    winery: str
    wine: str
    location: str
    image: str


class WineCreate(WineBase):
    rating: RatingCreate
    pass


class WineUpdate(WineBase):
    id: UUID
    rating: RatingUpdate
    pass


class WineModel(WineBase):
    id: UUID
    rating: RatingModel | None = None
    created_at: datetime

    class Config:
        from_attributes = True
