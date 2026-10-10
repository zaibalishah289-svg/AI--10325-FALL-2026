# Lab 04 — Python Data Structures & Clean Code

## Concepts Practiced
- Lists (Indexing, Slicing, Mutation, Append, Extend, Sorting)
- Tuples (Immutability, Unpacking, Multiple Return Values, Hashability, Dictionary Keys)
- Dictionaries (Structured Records, Safe Retrieval with `.get()`, Nested Dictionaries, Iteration)
- Sets (Unique Values, Set Operations: Union `|`, Intersection `&`, Difference `-`, Data Validation)
- Comprehensions (List, Dictionary, and Set Comprehensions for Filtering & Transformation)
- Iteration Tools (`enumerate()` with custom start index, `zip()` for parallel evaluation)
- Sorting and Counting Records
- Data Structure Selection & Architectural Modeling
- Clean Code (Modular Functions, Named Constants, Avoiding Side Effects)
- File Organization (`main.py`, `preprocessing.py`, `analysis.py`)

## Tasks Completed
1. **Lists**: Implemented list manipulation, slicing, finding indices, and counting threshold-compliant elements (`task01_lists.py`).
2. **Aliasing vs Copying**: Explored memory references, variable aliasing, independent shallow copies (`.copy()`), and deep copies (`copy.deepcopy()`) for nested structures (`task02_copying.py`).
3. **Tuples**: Practiced tuple unpacking, returning multiple values from functions, and utilizing tuples as hashable dictionary keys (`task03_tuples.py`).
4. **Dictionaries**: Created structured metadata records, safely queried missing keys using `.get()`, and handled nested metrics dictionaries (`task04_dictionaries.py`).
5. **Sets**: Extracted unique labels, performed set operations (`&`, `-`, `|`), and compared label sets (`task05_sets.py`).
6. **Comprehensions**: Refactored filtering and normalization logic using list, dictionary, and set comprehensions (`task06_comprehensions.py`).
7. **`enumerate()` & `zip()`**: Used iteration tools for indexed logging and parallel prediction-actual accuracy evaluations (`task07_iteration_tools.py`).
8. **Data Structure Selection**: Evaluated various AI modeling scenarios and mapped them to optimal Python data structures (`task08_data_modeling.py`).
9. **Prediction Analysis (Refactor & Extend)**: Restructured a messy monolithic script into a clean modular package (`main.py`, `preprocessing.py`, `analysis.py`) and extended it to handle missing/inconsistent batch records (`task09_clean_code/`).

## Data Structure Decisions
- **Scenario A (Ordered model names)**: Chosen `list` because insertion order and sequential evaluation history must be strictly preserved.
- **Scenario B (Fixed image size 224x224)**: Chosen `tuple` because dimensions are fixed, immutable data containers.
- **Scenario C (Model metadata attributes)**: Chosen `dictionary` to map descriptive string keys to structured attributes.
- **Scenario D (Unique class labels)**: Chosen `set` to guarantee uniqueness and efficient membership testing.
- **Scenario E (Multiple prediction records)**: Chosen a `list of dictionaries` to represent a collection of structured tabular records.
- **Scenario F (Comparing allowed vs received labels)**: Chosen `set` to perform high-speed set difference and intersection operations.

## Aliasing vs Copying
In Task 2, assigning `processed_scores = original_scores` created an alias pointing to the same memory reference, causing mutations in one to affect the other. Using `.copy()` solved this for flat lists. However, in Part C, `.copy()` performed only a shallow copy—inner dictionaries were still shared references, meaning mutating a nested dictionary updated the original data. `copy.deepcopy()` was required to recursively duplicate nested structures and achieve true isolation.

## Hashability
A tuple can be used as a dictionary key because it is **immutable** and therefore **hashable** (its hash value remains constant throughout its lifecycle). A list is **mutable**; if its contents were modified after being placed in a hash table, its hash value would change, breaking dictionary lookups. Consequently, Python raises a `TypeError: unhashable type: 'list'` when attempting to use lists as keys.

## Sets vs Lists for Validation
Sets are significantly better than lists for checking unexpected class labels. From a **clarity** perspective, set operators (`-`, `&`, `|`) directly express mathematical intent. From a **speed** perspective, set membership tests ($O(1)$ average time complexity via hash tables) vastly outperform list linear scans ($O(n)$ time complexity).

## Clean-Code Refactoring
- **What was difficult to read in original code**: Monolithic code, arbitrary single-letter variable names (`x`, `y`, `z`, `d`), magic numbers, and mixed responsibilities.
- **What you changed**: Extracted clean modular functions with meaningful names, introduced named constants (`MIN_CONFIDENCE`, `ALLOWED_LABELS`), and separated data input/coordination (`main.py`) from processing logic (`preprocessing.py` and `analysis.py`).
- **How you confirmed behavior did not change**: Verified that the refactored output metrics exactly matched the baseline values.
- **Why the refactored version is easier to maintain**: Functions have a single clear responsibility, operate on explicit inputs returning new values instead of mutating inputs, and decouple business logic from orchestration.

## Handling Incomplete Records
In Task 9 Part B, records missing mandatory fields (like `confidence`) were filtered out and their IDs were reported rather than silently dropped, maintaining auditability. Inconsistent capitalization and surrounding whitespace in labels were cleaned via `normalize_labels()` which safely utilized `.copy()` to protect raw inputs from unintended side effects.

## Edge Cases Tested
1. **Empty dataset passed to score summaries**: Verified that `summarize_scores([])` safely returns `None` instead of raising a ZeroDivisionError.
2. **Missing fields in prediction batches**: Confirmed that records lacking required keys are correctly isolated and logged in skipped IDs.
3. **Unrecognized external labels**: Verified that set difference accurately catches classes outside the allowed vocabulary.

## What I Found Difficult
Managing nested structures during deep copies and structuring modular imports across multiple package files required careful attention to path resolution and reference management.

## What I Learned
Advanced data structures (`tuples`, `dictionaries`, `sets`), memory reference isolation (`deepcopy`), and architectural separation of concerns significantly enhance code reliability and maintainability in AI pipelines.

## AI Engineering Relevance
- **Preprocessing**: Clean data normalization and validation ensure input integrity for downstream models.
- **Configuration**: Named constants and structured dictionaries manage system parameters cleanly.
- **Model Outputs**: Tuples and dictionaries structure predictions and performance metrics effectively.
- **Validation**: Set operations provide rapid classification label checking and anomaly detection.
- **Maintainability**: Modular design (`main`, `preprocessing`, `analysis`) ensures codebases scale seamlessly in production AI environments.