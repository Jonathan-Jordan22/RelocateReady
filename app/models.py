from sqlalchemy import Column, Integer, String, Float
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    country = Column(String, nullable=False)
    cost_index = Column(Float, nullable=True)
    safety_index = Column(Float, nullable=True)

class UserPreferences(Base):
    __tablename__ = "user_preferences"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    cost_index_weight = Column(Float, default=0.5)
    safety_index_weight = Column(Float, default=0.5)
    climate_importance = Column(Float, default=0.5)
    healthcare_importance = Column(Float, default=0.5)