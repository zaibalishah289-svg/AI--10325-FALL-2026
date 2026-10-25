# Lab 05 – NumPy & Numerical Computing for AI

## Environment
- Python version: 3.10+
- NumPy version: 1.24+

## Concepts Practiced
- NumPy arrays and shapes
- Indexing and slicing
- Views and copies
- Vectorization
- Broadcasting and axis
- Boolean masks and np.where
- Numerical transformations
- Matrix multiplication

## Tasks Completed
1. Array Basics
2. Indexing, Shapes, and Reshaping
3. Views and Copies
4. Vectorization and Dtypes
5. Broadcasting and Aggregation
6. Masks and Conditions
7. Feature Calculations
8. Sensor Feature Preparation

## Shape Reasoning
1. `features.mean(axis=0)` produces shape `(3,)` because aggregation collapses 4 sample rows into single feature averages.
2. `features.mean(axis=1)` produces shape `(4,)` because aggregation collapses 3 feature columns into single row averages.
3. `row_offsets.reshape(4, 1)` changes shape from `(4,)` to `(4, 1)`, allowing NumPy to broadcast across columns resulting in a `(4, 3)` matrix when added to `features`.

## Testing and Numerical Checks
| Task | Case | Expected | Actual | Pass/Fail |
| --- | --- | --- | --- | --- |
| Task 4 | Temp conversion | Equivalent values | Matches Python loop | Pass |
| Task 5 | Offsets addition | (4, 3) matrix | (4, 3) matrix | Pass |
| Task 6 | Validity range [0, 1] | 5 valid items | 5 valid items | Pass |
| Task 7 | Constant feature scaling | No zero div / NaN | 0.0 assigned | Pass |
| Task 8 | Sensor pipeline | 5 valid rows out of 8 | 5 valid rows | Pass |

## View vs Copy
In NumPy, `b = a[:3]` creates a **view**, meaning modifications to `b` directly alter the original array `a` as they share the same memory pointer. In contrast, `b = a[:3].copy()` creates an independent memory allocation, ensuring changes in `b` do not mutate original array `a`.

## Vectorization
In Task 4, temperature conversion was converted from a standard Python `for` loop into a single NumPy vectorized expression `(c_array * 9/5) + 32`. Vectorization eliminates loop overhead in Python and executes operations via compiled C-level loops.

## Sensor Pipeline Design
- **Function responsibilities:** `clean_sensor_rows` filters invalid range data; `summarize_features` extracts statistical metrics; `minmax_scale` normalizes values into `[0, 1]`; `flag_for_review` flags edge cases.
- **Input and output shapes:** Raw input shape `(8, 3)` -> Cleaned output shape `(5, 3)`.
- **Why invalid rows were removed:** Out-of-bound values distort statistical feature scaling and degrade model inference accuracy.
- **How constant features are handled:** Zero spans are replaced with `1.0` in division and explicitly set to `0.0` to avoid division-by-zero or NaN output.
- **What should happen when no valid rows remain:** A `ValueError` is raised to signal insufficient valid batch data.

## Challenges and Debugging
- **One problem I encountered:** Direct addition of `(4,)` array to `(4, 3)` matrix caused a broadcasting `ValueError`.
- **How I identified it:** Checked array `.shape` attributes before operation execution.
- **How I fixed it:** Used `.reshape(4, 1)` to align trailing matrix dimensions for broadcasting.

## AI Engineering Relevance
NumPy vectorized operations and broadcasting form the foundational mechanics of preprocessing pipelines, tensor operations, matrix multiplications, and loss/gradient calculations across modern Machine Learning and Deep Learning frameworks like PyTorch and TensorFlow.