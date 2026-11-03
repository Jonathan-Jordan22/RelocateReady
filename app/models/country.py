from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    code = Column(String(2), unique=True, nullable=False)
    currency = Column(String(3), nullable=False)

    locations = relationship("Location", back_populates="country_details")
    visa_options = relationship("VisaOption", back_populates="country")
