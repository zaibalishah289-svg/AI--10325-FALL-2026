# Reusable Score Utilities Module

def calculate_average(scores):
    """Calculates average score, returning None if list is empty."""
    if not scores:
        return None
    return sum(scores) / len(scores)

def is_passing(score, passing_score=50):
    """Checks if a single score meets the passing criteria."""
    return score >= passing_score

def count_above_threshold(scores, threshold):
    """Counts how many scores are greater than or equal to threshold."""
    count = 0
    for score in scores:
        if score >= threshold:
            count += 1
    return count

# Main guard demo block
if __name__ == "__main__":
    print("--- Running score_utils.py directly (Demo Mode) ---")
    demo_scores = [70, 80, 90]
    print("Demo Average:", calculate_average(demo_scores))
    print("Is 60 Passing?:", is_passing(60))
    print("Count >= 75:", count_above_threshold(demo_scores, 75))