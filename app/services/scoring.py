def calculate_relocation_score(user_preferences, location):
    """
    Calculate a weighted relocation score for a location.
    
    user_preferences:
        - can be either:
            1) a UserPreferences object from the database
            2) a ScoreRequest / dict with weights (for POST /score)
    location:
        - Location object from DB
    """
    total_weight = 0
    weighted_score = 0

    # Cost of living
    cost_weight = getattr(user_preferences, "cost_importance", getattr(user_preferences, "cost_index_weight", 0.5))
    cost_score = max(0, 100 - getattr(location, "average_rent", getattr(location, "cost_index", 0)) / 50)
    weighted_score += cost_score * cost_weight
    total_weight += cost_weight

    # Safety
    safety_weight = getattr(user_preferences, "safety_importance", getattr(user_preferences, "safety_index_weight", 0.5))
    safety_score = getattr(location, "safety_index", 0)
    weighted_score += safety_score * safety_weight
    total_weight += safety_weight

    # Climate
    climate_weight = getattr(user_preferences, "climate_importance", 0)
    climate_score = getattr(location, "climate_score", 0)
    weighted_score += climate_score * climate_weight
    total_weight += climate_weight

    # Healthcare
    healthcare_weight = getattr(user_preferences, "healthcare_importance", 0)
    healthcare_score = getattr(location, "healthcare_quality", 0)
    weighted_score += healthcare_score * healthcare_weight
    total_weight += healthcare_weight

    if total_weight == 0:
        return 0

    return round(weighted_score / total_weight, 2)