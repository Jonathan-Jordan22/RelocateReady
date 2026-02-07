def calculate_relocation_score(user_preferences, location):
    total_weight = 0
    weighted_score = 0

    # Cost of living
    cost_weight = user_preferences.cost_importance
    cost_score = max(0. 100 - location.average_rent / 50)
    weighted_score += cost_score * cost_weight
    total_weight += cost_weight

    # Safety
    safety_weight = user_preferences.safety_importance
    weighted_score += location.safety_index * safety_weight
    total_weight += safety_weight

    # Climate
    climate_weight = user_preferences.climate_importance
    weighted_score += location.climate_score * climate_weight
    total_weight += climate_weight

    # Healthcaree
    healthcare_weight = user_preferences.healthcare_importance
    weighted_score += location.healthcare_quality * healthcare_weight
    total_weight += healthcare_weight

    return round(weighted_score / total_weight, 2)