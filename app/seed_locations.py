from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Location

def seed_locations():
    db: Session = SessionLocal()

    locations = [
        # UK
        {"name": "Edinburgh", "country": "Scotland", "cost_index": 65, "safety_index": 78},
        {"name": "Glasgow", "country": "Scotland", "cost_index": 60, "safety_index": 70},
        {"name": "London", "country": "England", "cost_index": 85, "safety_index": 72},

        # Ireland
        {"name": "Dublin", "country": "Ireland", "cost_index": 80, "safety_index": 75},
        {"name": "Cork", "country": "Ireland", "cost_index": 68, "safety_index": 77},

        # Netherlands
        {"name": "Amsterdam", "country": "Netherlands", "cost_index": 82, "safety_index": 80},
        {"name": "Utrecht", "country": "Netherlands", "cost_index": 75, "safety_index": 82},

        # Australia
        {"name": "Melbourne", "country": "Australia", "cost_index": 78, "safety_index": 76},
        {"name": "Brisbane", "country": "Australia", "cost_index": 70, "safety_index": 74},

        # Canada
        {"name": "Toronto", "country": "Canada", "cost_index": 77, "safety_index": 73},
        {"name": "Vancouver", "country": "Canada", "cost_index": 85, "safety_index": 75},
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
