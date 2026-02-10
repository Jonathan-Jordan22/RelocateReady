from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models import Location

def seed_locations():
    # Create all tables first
    Base.metadata.create_all(bind=engine)
    
    db: Session = SessionLocal()

    locations = [
        # UK
        {"name": "Edinburgh", "country": "Scotland", "description": "Scotland's historic capital blends medieval charm with modern culture. Known for its stunning castle, festivals, and thriving tech scene.", "cost_index": 65, "safety_index": 78, "climate_index": 55, "healthcare_index": 85},
        {"name": "Glasgow", "country": "Scotland", "description": "A vibrant city with rich industrial heritage, world-class museums, and a thriving arts scene. More affordable than Edinburgh with a welcoming community.", "cost_index": 60, "safety_index": 70, "climate_index": 52, "healthcare_index": 83},
        {"name": "London", "country": "England", "description": "One of the world's most diverse and dynamic cities. Offers unparalleled career opportunities, culture, and entertainment, though at a premium cost.", "cost_index": 85, "safety_index": 72, "climate_index": 60, "healthcare_index": 87},

        # Ireland
        {"name": "Dublin", "country": "Ireland", "description": "Ireland's capital is a hub for tech giants and startups. Rich literary history, friendly locals, and easy access to stunning countryside.", "cost_index": 80, "safety_index": 75, "climate_index": 58, "healthcare_index": 82},
        {"name": "Cork", "country": "Ireland", "description": "Ireland's second city offers a more relaxed pace with excellent food culture, nearby coastal beauty, and growing job opportunities.", "cost_index": 68, "safety_index": 77, "climate_index": 56, "healthcare_index": 80},

        # Netherlands
        {"name": "Amsterdam", "country": "Netherlands", "description": "Famous for its canals, cycling culture, and liberal atmosphere. Strong international community and excellent quality of life.", "cost_index": 82, "safety_index": 80, "climate_index": 62, "healthcare_index": 90},
        {"name": "Utrecht", "country": "Netherlands", "description": "A charming university city with medieval architecture. More affordable than Amsterdam while maintaining excellent Dutch quality of life.", "cost_index": 75, "safety_index": 82, "climate_index": 61, "healthcare_index": 89},

        # Australia
        {"name": "Melbourne", "country": "Australia", "description": "Australia's cultural capital known for coffee, arts, and sports. Offers great work-life balance with four distinct seasons.", "cost_index": 78, "safety_index": 76, "climate_index": 75, "healthcare_index": 84},
        {"name": "Brisbane", "country": "Australia", "description": "Queensland's sunny capital with a subtropical climate. Growing economy, outdoor lifestyle, and proximity to beaches and rainforests.", "cost_index": 70, "safety_index": 74, "climate_index": 80, "healthcare_index": 82},

        # Canada
        {"name": "Toronto", "country": "Canada", "description": "Canada's largest city is incredibly diverse with strong job market in finance and tech. Cold winters but vibrant year-round culture.", "cost_index": 77, "safety_index": 73, "climate_index": 50, "healthcare_index": 88},
        {"name": "Vancouver", "country": "Canada", "description": "Stunning natural beauty meets urban sophistication. Mild climate by Canadian standards, outdoor recreation, and Pacific Rim culture.", "cost_index": 85, "safety_index": 75, "climate_index": 65, "healthcare_index": 86},
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
