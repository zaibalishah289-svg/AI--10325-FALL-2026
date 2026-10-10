# Workflow Orchestration Script
from preprocessing import clean_scores
from analyzer import ScoreAnalyzer

def main():
    raw_scores = [78, -5, 92, 110, 67, 88]
    
    # Step 1: Clean Data
    cleaned_scores = clean_scores(raw_scores)
    
    # Step 2: Analyze Data
    analyzer = ScoreAnalyzer(cleaned_scores)
    avg = analyzer.average()
    qualified_count = analyzer.count_above(70)
    
    # Step 3: Print Output Summary
    print("--- Refactored Modular Pipeline Output ---")
    print("Raw Input Scores:", raw_scores)
    print("Cleaned Scores:", cleaned_scores)
    print(f"Average Score: {avg:.2f}" if avg is not None else "Average Score: None")
    print("Qualified Count (>=70):", qualified_count)

if __name__ == "__main__":
    main()