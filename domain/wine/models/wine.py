from uuid import uuid4
from sqlalchemy.orm import mapped_column, Mapped, relationship
from core.db import Base
from domain.wine.models.rating import Rating


class Wine(Base):
    __tablename__ = 'wine'

    id: Mapped[str] = mapped_column(primary_key=True, default=str(uuid4()))
    winery: Mapped[str]
    wine: Mapped[str]
    rating: Mapped["Rating"] = relationship("Rating", lazy='selectin')
    location: Mapped[str]
    image: Mapped[str]
