from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class UserPreferences(Base):
    __tablename__ = "user_preferences"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    cost_of_living_weight = Column(Integer)
    safety_weight = Column(Integer)
    healthcare_weight = Column(Integer)
    climate_preference = Column(String)
    visa_difficulty_tolerance = Column(Integer)