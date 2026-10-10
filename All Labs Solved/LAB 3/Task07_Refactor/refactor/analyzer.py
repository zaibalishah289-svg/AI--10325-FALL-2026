# Analysis Module: Responsible for computing metrics using ScoreAnalyzer class

class ScoreAnalyzer:
    def __init__(self, scores):
        self.scores = scores

    def average(self):
        if not self.scores:
            return None
        return sum(self.scores) / len(self.scores)

    def count_above(self, threshold):
        return sum(1 for score in self.scores if score >= threshold)

    def highest(self):
        return max(self.scores) if self.scores else None

    def lowest(self):
        return min(self.scores) if self.scores else None