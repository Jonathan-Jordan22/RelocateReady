from typing import List
from ..models import User, Location

def predict_best_locations(user: User, locations: List[Location], top_n: int = 3):
    """
    Placeholder for AI-based prediction of top relocation locations.
    Currently uses a weighted score.
    Future: integrate OpenAI or ML model.
    """
    from .scoring import calculate_relocation_score

    scored = []
    for loc in locations:
        score = calculate_relocation_score(user.preferences, loc)
        scored.append((score, loc.name))

    # Sort descending and return top N
    scored.sort(key=lambda x: x[0], reverse=True)
    return [loc for score, loc in scored[:top_n]]
