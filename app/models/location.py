from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
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
    avg_rent_usd = Column(Integer, nullable=True)             # 1-bedroom, city centre, per month
    monthly_living_cost_usd = Column(Integer, nullable=True)  # per person, excluding rent
    cost_data_as_of = Column(Date, nullable=True)