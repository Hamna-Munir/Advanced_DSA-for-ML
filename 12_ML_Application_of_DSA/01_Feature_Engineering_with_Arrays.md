# Feature Engineering with Arrays

## 1. Concept Explanation
**Feature Engineering** is the process of transforming raw data into meaningful inputs (features) that improve the performance of machine learning models.

Arrays play a fundamental role in feature engineering because most machine learning libraries represent data as **arrays or matrices**. Each row usually represents a **data sample**, and each column represents a **feature**.

Using arrays, we can perform operations such as:

- Scaling numerical values
- Encoding categorical variables
- Creating new features
- Aggregating statistics
- Transforming data distributions

Efficient array manipulation is essential for preparing data before training machine learning models.

---

## 2. Visual / Example

Example dataset:

| Age | Salary |
|-----|--------|
| 22  | 30000  |
| 25  | 35000  |
| 30  | 50000  |
| 35  | 65000  |

Array representation:

[22, 30000]

[25, 35000]

[30, 50000]

[35, 65000]

We can create a new feature such as **Salary per Age**:

salary_per_age = salary / age

New feature array:

[1363]

[1400]

[1666]

[1857]


This new feature may help a machine learning model capture relationships more effectively.

---

## 3. Time & Space Complexity

For array operations with **n data samples** and **m features**:

- Feature transformation time complexity: **O(n × m)**
- Space complexity: **O(n × m)**

Efficient array operations help maintain scalable machine learning pipelines.

---

## 4. Python Code

### Feature Engineering with NumPy Arrays

```python
import numpy as np

# Dataset: Age and Salary
data = np.array([
    [22, 30000],
    [25, 35000],
    [30, 50000],
    [35, 65000]
])

age = data[:, 0]
salary = data[:, 1]

# Create a new feature
salary_per_age = salary / age

print("Salary per Age Feature:")
print(salary_per_age)
```
### Output
```python
Salary per Age Feature:
[1363.63 1400.   1666.67 1857.14]
```
### Feature Scaling Example

```python
import numpy as np

salary = np.array([30000, 35000, 50000, 65000])

scaled_salary = (salary - salary.mean()) / salary.std()

print("Scaled Salary:")
print(scaled_salary)
```

### Output
```python
Scaled Salary:
[-1.09 -0.73  0.36  1.46]
```
---

## 5. Common Interview Problems

- Normalize a dataset using arrays

- Compute statistical features (mean, variance)

- Sliding window feature extraction

- Feature scaling and transformation

- Implement moving average

These problems test understanding of array manipulation and data preprocessing.

---

## 6. ML Connection

Feature engineering is one of the most critical steps in machine learning.

Arrays are used in:

- NumPy numerical computation

- Pandas data preprocessing

- Tensor representations in deep learning

- Matrix-based model training

- Batch data processing

Well-designed features often improve model performance more than changing algorithms.

---

## 7. Practice Tasks

1. Create a feature representing salary growth rate

2. Normalize a dataset using min-max scaling

3. Compute mean, variance, and standard deviation using arrays

4. Create polynomial features

5. Implement a moving average feature

Practicing these tasks helps build strong data preprocessing skills.

---

**Author:**  
Hamna Munir
