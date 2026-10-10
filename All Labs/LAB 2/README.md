# Lab 02 — Python Fundamentals for Problem Solving

**Course:** AI-216: Programming for Artificial Intelligence  
**Semester:** Fall 2026  
**Author:** Ali  
**Repository:** Coursework Repository  

---

## 1. Overview & Objectives
This repository contains the complete implementation of **Lab 02: Python Fundamentals for Problem Solving**[cite: 3]. The primary goal of this lab is to build strong Python logic-building foundations required for core Artificial Intelligence and Data Science workflows[cite: 3].

### Concepts Practiced:
* **Variables & Data Types:** Managing structured and primitive values[cite: 3, 26].
* **Operators:** Arithmetic, comparison, and boolean evaluation[cite: 3, 26].
* **Conditionals:** Decision trees using `if`, `elif`, and `else` constructs[cite: 3, 26].
* **Iterative Loops:** Sequential data traversal using `for` loops[cite: 3, 26].
* **Modular Functions:** Encapsulating logic with `def`, input parameters, and return values[cite: 3, 26].
* **Problem Decomposition:** Breaking complex tasks into structured input-processing-output stages[cite: 3, 21].

---

## 2. Tasks Completed

### Task 1: Daily Expense Tracker (`task01_expense_tracker.py`)
* **Objective:** Calculate student spending against a daily budget and determine budget status[cite: 7].
* **Implementation:** Computed total expenses and remaining balance using integer types, applying conditionals for `Within budget`, `Exactly at budget`, and `Over budget` classifications[cite: 7, 8].

### Task 2: Internet Package Advisor (`task02_package_advisor.py`)
* **Objective:** Recommend internet packages based on monthly data usage[cite: 9, 10].
* **Implementation:** Converted dynamic user input to `float`, validated negative values, and mapped thresholds (Basic: 0–5GB, Standard: 5–15GB, Premium: >15GB)[cite: 10, 11].

### Task 3: Temperature Monitoring (`task03_temperature_monitor.py`)
* **Objective:** Categorize thermal sensor readings into Below Normal, Normal, and High categories[cite: 12].
* **Implementation:** Iterated through temperature floats using a `for` loop, updating accumulators and outputting formatted count summaries[cite: 12, 13].

### Task 4: Model Score Analysis (`task04_score_analysis.py`)
* **Objective:** Evaluate AI model prediction accuracy scores against a performance benchmark[cite: 13, 14].
* **Implementation:** Implemented accumulator-based average and target percentage calculations with 2-decimal formatting, including empty-list validation to prevent division errors[cite: 14, 15].

### Task 5: Applicant Eligibility (`task05_applicant_eligibility.py`)
* **Objective:** Determine candidate eligibility based on multi-criterion prerequisites[cite: 15, 16].
* **Implementation:** Used independent `if` statements to evaluate age ($\ge 18$), score ($\ge 60$), and prerequisite status, reporting every specific requirement failed[cite: 15, 16, 17].

### Task 6: Refactor Logic into Functions (`task06_functions.py`)
* **Objective:** Convert imperative task logic into clean, reusable Python functions[cite: 17, 18].
* **Implementation:** Defined pure functions (`calculate_percentage`, `is_passing`, `count_values_above_threshold`) returning boolean and numerical values without internal side-effects[cite: 17, 18].

### Task 7: Problem Decomposition Challenge (`task07_decomposition.py`)
* **Objective:** Option A — Electricity Usage Classification[cite: 19].
* **Implementation:** Structured problem header into Problem, Inputs, Rules, Repetition, and Outputs, processing daily kWh usage and computing formatted summary metrics[cite: 19, 21].

---

## 3. Boundary & Test Case Results

| Task | Input Case / Data | Expected Output | Actual Output | Status |
| :--- | :--- | :--- | :--- | :---: |
| **Task 1** | Food: 450, Transport: 200, Other: 150, Budget: 1000 | Total: 800, Remaining: 200 (Within budget) | Total: 800, Remaining: 200 (Within budget) | ✅ Pass |
| **Task 2** | Usage: `5.0` GB | Recommended Package: Basic | Recommended Package: Basic | ✅ Pass |
| **Task 2** | Usage: `5.1` GB | Recommended Package: Standard | Recommended Package: Standard | ✅ Pass |
| **Task 2** | Usage: `-1.0` GB | Invalid — usage cannot be negative | Invalid — usage cannot be negative | ✅ Pass |
| **Task 3** | `[21.5, 29.0, 32.5, 18.0, 35.2, 27.8, 14.0]` | Below Normal: 1, Normal: 4, High: 2 | Below Normal: 1, Normal: 4, High: 2 | ✅ Pass |
| **Task 4** | Scores: `[0.72, 0.81, 0.88, 0.91, 0.67, 0.86, 0.79]`, Threshold: `0.85` | Avg: 0.81, Target Meeting: 42.86% | Avg: 0.81, Target Meeting: 42.86% | ✅ Pass |
| **Task 5** | Age: 17, Score: 55, Prerequisite: False | Not eligible (Reports all 3 unmet conditions) | Not eligible (Reports all 3 unmet conditions) | ✅ Pass |

---

## 4. Engineering Reflections & Lessons Learned

### Key Challenges & Solutions:
1. **Handling Edge/Boundary Conditions:** Ensuring inclusive checks ($\le$ vs $<$) on boundary metrics like data usage boundaries (5.0 vs 5.1 GB) required precise conditional order[cite: 10, 23].
2. **Multiple Unmet Requirements:** Standard `if-elif-else` chains terminate at the first true condition[cite: 16]. Switching to independent `if` statements allowed reporting *all* failed eligibility requirements simultaneously[cite: 16, 17].
3. **Pure Function Design:** Ensuring functions only return computed values rather than printing directly enforced modular coding practices[cite: 18].

### Relevance to AI Engineering:
* **Data Preprocessing & Filtering:** Conditional filtering and threshold checks emulate real-world data cleansing pipelines before feeding data into Machine Learning models[cite: 27].
* **Model Evaluation Metrics:** Calculating accuracy percentages and average scores directly mirrors model validation evaluation scripts[cite: 27].
* **Input Validation:** Rejecting invalid inputs (e.g., negative usage or empty score lists) ensures robustness in AI deployment microservices[cite: 10, 15, 27].

---

## 5. Submission Checklist Verification
- [x] All required `.py` scripts exist in the repository[cite: 28].
- [x] All scripts run without runtime or syntax errors[cite: 28].
- [x] Descriptive variable naming conventions used throughout[cite: 28].
- [x] Boundary cases tested and verified[cite: 28].
- [x] Functions return pure output without unintended printing[cite: 28].
- [x] Floating point numbers formatted to 2 decimal places[cite: 6, 28].
- [x] Structured Git commit history maintained per task.s