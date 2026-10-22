from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base


class UserLocation(Base):
    __tablename__ = "user_locations"
    __table_args__ = (
        UniqueConstraint("user_id", "location_id", name="uq_user_location"),
    )

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)

    # Relationships
    location = relationship("Location", backref="user_locations")
