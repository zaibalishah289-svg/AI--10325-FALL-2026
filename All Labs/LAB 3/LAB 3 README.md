# Lab 03 — Functions, Modules, Exceptions, Debugging & OOP

## Concepts Practiced
- Functions
- Scope
- Modules and imports
- `if __name__ == "__main__"`
- Exception handling
- Debugging
- Classes and objects
- Refactoring

## Tasks Completed
1. **Function Design:** Built reusable score calculation and classification functions[cite: 7, 8, 9].
2. **Scope:** Observed local vs. global scope variable behavior and refactored global state dependencies[cite: 10, 11, 12].
3. **Modules:** Created custom `score_utils` module and imported it into `main.py` using `if __name__ == "__main__":` guard[cite: 13, 14, 15].
4. **Exception Handling:** Implemented defensive parameter checks using `raise ValueError` and handled runtime errors using `try/except/else/finally`[cite: 16, 17, 18].
5. **Debugging Challenge:** Identified and resolved calculation loop accumulation errors (`+=`) and conditional precedence bugs in `classify()`[cite: 19, 20].
6. **ScoreAnalyzer Class:** Built an Object-Oriented score analyzer class encapsulating internal state and analysis methods[cite: 21, 22, 23].
7. **Refactoring Task:** Refactored procedural code into modular files (`preprocessing.py`, `analyzer.py`, `main.py`) adhering to separation of concerns[cite: 26, 27, 28].

## Debugging Notes
- **One bug found:** In `calculate_average()`, the loop was using `total = score` instead of `total += score`, causing it to overwrite the total instead of accumulating it[cite: 19, 20].
- **How I located it:** By inspecting the unexpected output (average returning as 22.5 instead of 75.0) and tracing variable values inside the loop[cite: 20, 21].
- **How I fixed it:** Changed `total = score` to `total += score`. Additionally, reordered conditions in `classify()` so `>= 85` is checked before `>= 50`[cite: 20].

## Exception Handling Test Cases
| Case | Input | Expected Result | Actual Result |
| :--- | :--- | :--- | :--- |
| **Valid** | `obtained = 80, total = 100` | Success (80.00%) | Success (80.00%) |
| **Invalid (Negative)** | `obtained = -5, total = 100` | ValueError: Negative marks | Error caught: Obtained marks cannot be negative. |
| **Invalid (Exceeds)** | `obtained = 120, total = 100` | ValueError: Obtained > Total | Error caught: Obtained marks cannot be greater than total marks. |
| **Boundary (Zero Total)** | `obtained = 80, total = 0` | ValueError: Total <= 0 | Error caught: Total marks must be strictly greater than 0. |
| **Text Input** | `obtained = "eighty", total = 100` | ValueError: Conversion Error | Error caught: could not convert string to float: 'eighty' |

## Design Decisions
- **Why did you use functions in some places?** Functions were used for pure computations without persistent state (e.g., calculating averages or filtering values) to ensure modular reusability[cite: 33, 34].
- **Why did you use a class in Task 6/7?** A class was used because data (`self.scores`) and behavior (`clean()`, `average()`, `count_above()`) belonged together, allowing safe internal state management[cite: 22, 23, 34].
- **What logic belongs in `main.py`?** `main.py` handles higher-level workflow orchestration and user display, keeping business logic and data cleaning inside dedicated modules[cite: 27, 28, 29].

## What I Found Difficult
Handling relative imports across custom sub-folders and ensuring exception boundaries handled non-numeric strings smoothly.

## What I Learned
How to design modular Python code, isolate local/global scopes, handle runtime errors gracefully, and write clean Object-Oriented code suitable for production.

## AI Engineering Relevance
AI pipelines require clean data preprocessing modules, modular object structures for ML models, and robust error handling to prevent pipeline failures on bad input data[cite: 30, 31].