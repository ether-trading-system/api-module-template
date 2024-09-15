from pydantic import BaseModel, Field


class RatingModel(BaseModel):
    wine_id: str = Field()
