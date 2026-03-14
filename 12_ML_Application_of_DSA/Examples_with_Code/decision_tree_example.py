# Decision Tree Example
# Using Scikit-Learn

from sklearn.tree import DecisionTreeClassifier

# Features: [study_hours, attendance]
X = [
    [5, 1],
    [4, 1],
    [3, 1],
    [2, 0],
    [1, 0]
]

# Labels: Pass(1), Fail(0)
y = [1, 1, 1, 0, 0]

model = DecisionTreeClassifier()

model.fit(X, y)

prediction = model.predict([[2, 1]])

print("Prediction:", prediction)


# Output
# Prediction: [1]
