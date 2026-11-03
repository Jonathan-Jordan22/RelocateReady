from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    country = Column(String, nullable=False)
    description = Column(String, nullable=True)
    cost_index = Column(Float, nullable=True)
    safety_index = Column(Float, nullable=True)
    climate_index = Column(Float, nullable=True)
    healthcare_index = Column(Float, nullable=True)
    country_id = Column(Integer, ForeignKey("countries.id", name="fk_locations_country_id"), nullable=False)
    country_details = relationship("Country", back_populates="locations")
