from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import relationship

from app.database import Base


class VisaOption(Base):
    __tablename__ = "visa_options"
    __table_args__ = (
        UniqueConstraint("country_id", "name", name="uq_visa_country_name"),
    )

    id = Column(Integer, primary_key=True)
    country_id = Column(
        Integer,
        ForeignKey("countries.id", name="fk_visa_options_country_id"),
        nullable=False,
        index=True,
    )
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    summary = Column(Text, nullable=False)
    eligibility = Column(Text, nullable=False)
    estimated_cost_usd = Column(Integer, nullable=False)
    processing_time = Column(String,nullable=True)
    official_url = Column(String, nullable=False)
    last_verified = Column(Date, nullable=False)

    country = relationship("Country", back_populates="visa_options")