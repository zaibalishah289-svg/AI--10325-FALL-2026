# Task 6: Object-Oriented Programming with ScoreAnalyzer Class

class ScoreAnalyzer:
    def __init__(self, scores):
        self.scores = scores

    def clean(self):
        # Keep only values between 0 and 100 inclusive
        self.scores = [score for score in self.scores if 0 <= score <= 100]

    def average(self):
        if not self.scores:
            return None
        return sum(self.scores) / len(self.scores)

    def count_above(self, threshold):
        return sum(1 for score in self.scores if score >= threshold)

    def summary(self):
        if not self.scores:
            return {"count": 0, "average": None, "highest": None, "lowest": None}
        return {
            "count": len(self.scores),
            "average": round(self.average(), 2),
            "highest": max(self.scores),
            "lowest": min(self.scores)
        }

# Test execution with raw dataset
if __name__ == "__main__":
    raw_scores = [78, -5, 110, 67, 90, 88]
    analyzer = ScoreAnalyzer(raw_scores)
    
    print("Initial Raw Scores:", analyzer.scores)
    analyzer.clean()
    print("Cleaned Scores:", analyzer.scores)
    print("Calculated Average:", analyzer.average())
    print("Count Above 80:", analyzer.count_above(80))
    print("Summary Dictionary:", analyzer.summary())