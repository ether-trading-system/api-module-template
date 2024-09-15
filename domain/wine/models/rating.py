from sqlalchemy import Column, ForeignKey, Float
from sqlalchemy.orm import mapped_column, Mapped
from core import Base


class Rating(Base):
    __tablename__ = 'rating'

    id: Mapped[int] = mapped_column(primary_key=True)
    wind_id: Mapped[str] = mapped_column(ForeignKey('wine.id'))
    average: Mapped[float] = Column(Float)
    reviews = Column(Float)
