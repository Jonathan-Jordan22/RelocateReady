from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models import Location

def seed_locations():
    # Create all tables first
    Base.metadata.create_all(bind=engine)
    
    db: Session = SessionLocal()

    locations = [
        # UK
        {"name": "Edinburgh", "country": "Scotland", "cost_index": 65, "safety_index": 78, "climate_index": 55, "healthcare_index": 85},
        {"name": "Glasgow", "country": "Scotland", "cost_index": 60, "safety_index": 70, "climate_index": 52, "healthcare_index": 83},
        {"name": "London", "country": "England", "cost_index": 85, "safety_index": 72, "climate_index": 60, "healthcare_index": 87},

        # Ireland
        {"name": "Dublin", "country": "Ireland", "cost_index": 80, "safety_index": 75, "climate_index": 58, "healthcare_index": 82},
        {"name": "Cork", "country": "Ireland", "cost_index": 68, "safety_index": 77, "climate_index": 56, "healthcare_index": 80},

        # Netherlands
        {"name": "Amsterdam", "country": "Netherlands", "cost_index": 82, "safety_index": 80, "climate_index": 62, "healthcare_index": 90},
        {"name": "Utrecht", "country": "Netherlands", "cost_index": 75, "safety_index": 82, "climate_index": 61, "healthcare_index": 89},

        # Australia
        {"name": "Melbourne", "country": "Australia", "cost_index": 78, "safety_index": 76, "climate_index": 75, "healthcare_index": 84},
        {"name": "Brisbane", "country": "Australia", "cost_index": 70, "safety_index": 74, "climate_index": 80, "healthcare_index": 82},

        # Canada
        {"name": "Toronto", "country": "Canada", "cost_index": 77, "safety_index": 73, "climate_index": 50, "healthcare_index": 88},
        {"name": "Vancouver", "country": "Canada", "cost_index": 85, "safety_index": 75, "climate_index": 65, "healthcare_index": 86},
    ]

    for loc in locations:
        exists = db.query(Location).filter(
            Location.name == loc["name"],
            Location.country == loc["country"]
        ).first()

        if not exists:
            db.add(Location(**loc))

    db.commit()
    db.close()

if __name__ == "__main__":
    seed_locations()
