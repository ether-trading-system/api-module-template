from pydantic import BaseModel

class WineModel(BaseModel):
    id: int
    winery: str
    wine: str
    rating: dict
    location: str
    image: str