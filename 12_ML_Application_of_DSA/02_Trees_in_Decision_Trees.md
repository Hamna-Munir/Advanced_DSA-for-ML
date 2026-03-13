# Trees in Decision Trees

## 1. Concept Explanation
A **Decision Tree** is a machine learning model that uses a **tree data structure** to make predictions based on input features.

The structure of a decision tree is similar to a real tree and consists of:

- **Root Node** — the top node where the first decision is made
- **Internal Nodes** — nodes that represent feature-based conditions
- **Leaf Nodes** — final prediction outcomes

Each internal node represents a **decision rule**, and each branch represents the outcome of that rule.

Decision trees work by **recursively splitting the dataset** based on the best feature that separates the data.

This process continues until the algorithm reaches a stopping condition, such as:

- Maximum tree depth
- Minimum number of samples
- Pure leaf nodes

Decision trees are widely used for both:

- **Classification**
- **Regression**

---

## 2. Visual / Example

Example: Predicting whether a student will **pass or fail** an exam.

```python
        Study Hours
       /           \
   > 3 hours      ≤ 3 hours
     /               \
  Pass            Attendance
                  /        \
              High          Low
               |             |
             Pass           Fail
```

Explanation:

- If **study hours > 3**, the student is predicted to **Pass**
- If **study hours ≤ 3**, the model checks **attendance**
- If attendance is **high → Pass**
- If attendance is **low → Fail**

The model follows a **path from root to leaf** to make a prediction.

---

## 3. Time & Space Complexity

For a dataset with **n samples** and **m features**:

Training Complexity (approximate):

- **O(n × m × log n)**

Prediction Complexity:

- **O(tree depth)**

Space Complexity:

- **O(n)**

Decision trees are efficient during prediction because they only traverse one path from the root to a leaf node.

---

## 4. Python Code

### Decision Tree Example (Using Scikit-Learn)

```python
from sklearn.tree import DecisionTreeClassifier

# Example dataset
# Features: [study_hours, attendance]
X = [
    [5, 1],
    [4, 1],
    [3, 1],
    [2, 0],
    [1, 0]
]

# Labels: 1 = Pass, 0 = Fail
y = [1, 1, 1, 0, 0]

model = DecisionTreeClassifier()

model.fit(X, y)

prediction = model.predict([[2, 1]])

print("Prediction:", prediction)
```

### Outpu
```python
Prediction: [1]
```
Explanation:

- Input: study_hours = 2, attendance = 1

- Output: Pass

### Simple Decision Tree Logic (Manual Implementation)
```python
def decision_tree(study_hours, attendance):

    if study_hours > 3:
        return "Pass"

    else:
        if attendance == 1:
            return "Pass"
        else:
            return "Fail"


result = decision_tree(2, 0)

print("Result:", result)
```
### Output
```python
Result: Fail
```
---


## 5. Common Interview Problems

- Implement a decision tree from scratch

- Calculate Gini Impurity

- Calculate Entropy and Information Gain

- Build classification trees

- Implement Random Forest using decision trees

These problems test understanding of tree structures and ML model logic.

---


## 6. ML Connection

Decision trees are one of the most important algorithms in machine learning.

They are used in:

- Decision Tree Classifiers

- Random Forest

- Gradient Boosted Trees

- XGBoost

- LightGBM

Applications include:

- Medical diagnosis

- Fraud detection

- Credit risk analysis

- Customer behavior prediction

- Recommendation systems

Tree-based models are powerful because they are interpretable and easy to understand.

---


## 7. Practice Tasks

1. Implement a decision tree classifier from scratch

2. Calculate entropy for a dataset

3. Compute information gain for feature selection

4. Visualize a decision tree using Python

5. Train a decision tree on a real dataset

Practicing these tasks strengthens understanding of tree-based machine learning models.

---

**Author:**  
Hamna Munir
