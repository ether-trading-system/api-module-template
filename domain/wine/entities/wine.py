from uuid import uuid4, uuid5, UUID
from sqlalchemy.orm import mapped_column, Mapped, relationship
from core.db import Base
from domain.wine.entities.rating import Rating


class Wine(Base):
    __tablename__ = 'wine'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    winery: Mapped[str]
    wine: Mapped[str]
    rating: Mapped["Rating"] = relationship("Rating", lazy='selectin')
    location: Mapped[str]
    image: Mapped[str]
