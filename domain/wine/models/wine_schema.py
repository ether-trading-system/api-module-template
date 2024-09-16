from datetime import datetime
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
    id: str
    rating: RatingUpdate
    pass


class WineModel(WineBase):
    id: str
    rating: RatingModel | None = None
    created_at: datetime

    class Config:
        orm_mode = True