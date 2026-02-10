# RelocateReady

A comprehensive relocation planning platform that helps users discover and evaluate international destinations based on personalized preferences.

## Overview

RelocateReady is a FastAPI-based backend service designed to assist individuals in making informed decisions about international relocations. The platform provides detailed information about cities worldwide, personalized scoring based on user preferences, and tools to save and compare potential destinations.

## Features

### User Management
- **Secure Authentication**: User registration with email/password and bcrypt encryption
- **Profile Management**: Update personal information (name, email)
- **User Preferences**: Customizable importance weights for relocation factors

### Location Database
- **Curated Destinations**: Pre-seeded database of popular relocation cities
- **Detailed Information**: Each location includes:
  - Cost of living index
  - Safety ratings
  - Climate scores
  - Healthcare quality metrics
  - Descriptive overviews

### Smart Scoring System
- **Personalized Rankings**: Locations scored based on user preferences
- **Custom Weightings**: Users control importance of cost, safety, climate, and healthcare
- **Saved Locations**: Build and rank a personalized list of potential destinations

### API Endpoints

#### Users
- `POST /users/` - Create new user account
- `POST /users/login` - User authentication
- `GET /users/{user_id}` - Retrieve user profile
- `PUT/PATCH /users/{user_id}` - Update user information
- `DELETE /users/{user_id}` - Delete user account

#### Locations
- `GET /locations/` - List all available locations
- `GET /locations/{location_id}` - Get detailed location information
- `POST /locations/` - Add new location (admin)

#### Preferences
- `GET /preferences/{user_id}` - Retrieve user preferences
- `POST /preferences/{user_id}` - Create or update preferences

#### User Locations
- `POST /user-locations/{user_id}/{location_id}` - Save location to user's list
- `GET /user-locations/{user_id}` - Get all saved locations
- `DELETE /user-locations/{user_id}/{location_id}` - Remove saved location

#### Scoring
- `POST /score/` - Score all locations with custom weights
- `GET /score/{user_id}/{location_id}` - Score specific location for user
- `POST /score/user/{user_id}/ranked` - Get ranked list of user's saved locations

## Technology Stack

- **Framework**: FastAPI
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: bcrypt password hashing
- **Validation**: Pydantic schemas
- **Python**: 3.13+

## Getting Started

### Prerequisites
- Python 3.13 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd relocateready
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate    # macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Seed the database:
```bash
python -m app.seed_locations
```

5. Run the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Project Structure

```
relocateready/
├── app/
│   ├── models/          # Database models
│   ├── routes/          # API endpoints
│   ├── schemas/         # Pydantic validation schemas
│   ├── services/        # Business logic
│   ├── utils/           # Helper functions
│   ├── database.py      # Database configuration
│   └── main.py          # FastAPI application
├── requirements.txt     # Project dependencies
└── README.md
```

## Default Preferences

New users are created with default preference values of `0.0` for all factors:
- Cost importance: 0.0
- Safety importance: 0.0
- Climate importance: 0.0
- Healthcare importance: 0.0

Users can customize these values via the preferences endpoint to reflect their personal priorities.

## Future Enhancements

- AI-powered location recommendations
- Additional location metrics (job market, culture, language)
- User reviews and ratings
- Visa requirement information
- Currency conversion and salary comparisons
- Weather data integration

## License

This project is available for educational and personal use.
