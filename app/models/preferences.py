from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Preferences(Base):
    __tablename__ = "preferences"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    
    cost_importance = Column(Float, default=0.5)
    safety_importance = Column(Float, default=0.5)
    climate_importance = Column(Float, default=0.0)
    healthcare_importance = Column(Float, default=0.0)

    user = relationship("User", back_populates="preferences")
