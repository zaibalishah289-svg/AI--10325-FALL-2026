# Preprocessing Module: Responsible for data validation and cleaning

def clean_scores(scores):
    """Filters raw scores to keep only valid values between 0 and 100 inclusive."""
    return [score for score in scores if 0 <= score <= 100]