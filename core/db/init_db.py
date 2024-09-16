from domain.wine.entities.rating import Rating
from .db import engine
from domain.wine.entities.wine import Wine


def create_tables():
    Wine.metadata.create_all(bind=engine)
    Rating.metadata.create_all(bind=engine)
