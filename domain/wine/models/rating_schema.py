from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class RatingBase(BaseModel):
    average: float
    reviews: float


class RatingCreate(RatingBase):
    pass


class RatingUpdate(RatingBase):
    pass


class RatingModel(RatingBase):
    id: int
    wine_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
