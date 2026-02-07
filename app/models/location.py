from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    country = Column(String, nullable=False)
    cost_index = Column(Float, nullable=True)
    safety_index = Column(Float, nullable=True)
