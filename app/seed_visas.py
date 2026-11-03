from datetime import date

from app.database import SessionLocal
from app.models import Country, VisaOption


VISAS = [
    {
        "country": "United Kingdom",
        "name": "Skilled Worker visa",
        "category": "work",
        "summary": "Work for a UK employer that is licensed to sponsor visa holders.",
        "eligibility": "Job offer from a Home Office-approved sponsor, meeting the salary and skill-level thresholds, plus an English language requirement.",
        "estimated_cost_usd": 7464,  
        "processing_time": "About 3 weeks from outside the UK",
        "official_url": "https://www.gov.uk/skilled-worker-visa",
        "last_verified": date(2026, 11, 3),
    },
    {
        "country": "United Kingdom",
        "name": "Global Talent visa",
        "category": "work",
        "summary": "Live and work in the UK without a job offer if you are a leader or emerging leader in your field.",
        "eligibility": "Endorsement from an approved body (or an eligible award) in academia/research, arts and culture, or digital technology.",
        "estimated_cost_usd": 3871,  
        "processing_time": None,
        "official_url": "https://www.gov.uk/global-talent",
        "last_verified": date(2026, 11, 3),
    },
    {
        "country": "Ireland",
        "name": "Critical Skills Employment Permit",
        "category": "work",
        "summary": "Employment permit for highly skilled roles, with a path to living and working in Ireland without a permit.",
        "eligibility": "A 2-year job offer: €40,904+ for occupations on the Critical Skills list (with a relevant degree), or €68,911+ for most other occupations.",
        "estimated_cost_usd": 1120,  
        "processing_time": "Apply at least 12 weeks before your start date",
        "official_url": "https://enterprise.gov.ie/en/what-we-do/workplace-and-skills/employment-permits/permit-types/critical-skills-employment-permit/",
        "last_verified": date(2026, 11, 3),
    },
    {
        "country": "Netherlands",
        "name": "DAFT (Dutch-American Friendship Treaty) residence permit",
        "category": "self_employed",
        "summary": "A residence permit for US citizens who start their own business or freelance in the Netherlands.",
        "eligibility": "US citizenship, a registered Dutch business, a business plan, and at least €4,500 kept in the business account.",
        "estimated_cost_usd": 474,  
        "processing_time": None,
        "official_url": "https://ind.nl/en/residence-permits/work/residence-permit-self-employed-person",
        "last_verified": date(2026, 11, 3),
    },
    {
        "country": "Australia",
        "name": "Work and Holiday visa (subclass 462)",
        "category": "working_holiday",
        "summary": "Spend up to a year in Australia, working to fund your travels.",
        "eligibility": "US citizens aged 18 to 30 at the time of application.",
        "estimated_cost_usd": 586, 
        "processing_time": None,
        "official_url": "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/work-holiday-462",
        "last_verified": date(2026, 11, 3),
    },
    {
        "country": "Canada",
        "name": "Express Entry (permanent residence)",
        "category": "permanent_residence",
        "summary": "Points-based permanent residence for skilled workers, managed through an online profile and invitation rounds.",
        "eligibility": "Points from age, education, language test results, and work experience. Foreign degrees need an Educational Credential Assessment.",
        "estimated_cost_usd": 1140, 
        "processing_time": None,
        "official_url": "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html",
        "last_verified": date(2026, 11, 3),
    },
]


def seed_visas():
    db = SessionLocal()
    added = updated = 0
    try:
        for visa in VISAS:
            if visa["last_verified"] is None:
                print(f"Skipping {visa['name']}: not verified yet")
                continue

            data = {k: v for k, v in visa.items() if k != "country"}
            country = db.query(Country).filter_by(name=visa["country"]).one()

            existing = db.query(VisaOption).filter_by(
                country_id=country.id, name=visa["name"]
            ).first()
            if existing:
                for key, value in data.items():
                    setattr(existing, key, value)
                updated += 1
            else:
                db.add(VisaOption(country_id=country.id, **data))
                added += 1

        db.commit()
        print(f"Visas seeded: {added} added, {updated} updated")
    finally:
        db.close()

if __name__ == "__main__":
    seed_visas()