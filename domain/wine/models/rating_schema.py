from datetime import datetime
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
    wine_id: str
    created_at: datetime

    class Config:
        from_attributes = True
