from domain.wine.models.rating import Rating
from .db import engine
from domain.wine.models.wine import Wine


def create_tables():
    Wine.metadata.create_all(bind=engine)
    Rating.metadata.create_all(bind=engine)
