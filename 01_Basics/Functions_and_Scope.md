# Functions and Scope

## 1. Concept Explanation 
Functions are **reusable blocks of code** designed to perform a specific task. Instead of repeating the same logic, functions allow you to write code once and use it multiple times.

Scope defines **where a variable can be accessed** in a program. Understanding scope is critical for writing predictable, bug-free code—especially in Machine Learning pipelines where multiple components interact.

---

## 2. Visual / Example

### Function
Think of a function as a machine:
- Input goes in (parameters)
- Processing happens
- Output comes out (return value)

### Scope
Think of scope as boundaries:
- **Local scope** → variables inside a function
- **Global scope** → variables defined outside functions

Variables cannot always cross these boundaries.

---

## 3. Time & Space Complexity
Functions themselves do not change time complexity, but:
- The **operations inside** a function determine time complexity
- Recursive functions can increase space complexity due to the call stack

Examples:
- A function with a loop over `n` elements → **O(n)**
- A recursive function → **O(n)** space (stack usage)

Understanding this helps optimize ML training and data-processing pipelines.

---

## 4. Python Code

### Defining a Function
```python
def calculate_loss(predicted, actual):
    return abs(predicted - actual)
```
### Local vs Global Scope
```python
learning_rate = 0.01  # Global variable

def update_rate():
    learning_rate = 0.001  # Local variable
    print(learning_rate)

update_rate()
print(learning_rate)
```
### Returning Values
```python
def square(x):
    return x * x

result = square(4)
```
---

## 5. Common Interview Problems

Common interview questions include:

- Difference between parameters and arguments

- Local vs global variables

- Default arguments in functions

- Function call stack

- Recursion vs iteration

Interviewers assess clarity of logic and scope awareness.

---

## 6. ML Connection

Functions are essential in Machine Learning:

- Data preprocessing functions

- Feature engineering pipelines

- Model training and evaluation functions

- Loss and metric calculations

Scope management prevents:

- Accidental overwriting of model parameters

- Hidden bugs in training loops

- Hard-to-debug ML pipeline errors

Clean function design leads to modular and maintainable ML systems.

---

## 7. Practice Tasks

1. Write a function to normalize a list of numbers

2. Create a function that calculates accuracy

3. Demonstrate local and global scope using variables

4. Write a recursive function and analyze its space complexity

5. Refactor repeated code into reusable functions

---

**Author:**  
Hamna Munir
