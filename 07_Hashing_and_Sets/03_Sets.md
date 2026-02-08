# Sets

## 1. Concept Explanation 
A **Set** is a data structure that stores **unique elements only**. It automatically removes duplicates and allows fast membership checking.

Sets are implemented using hashing internally, which makes operations like insertion, deletion, and lookup very efficient.

Sets are commonly used when you need to:
- Remove duplicates
- Check if an element exists
- Perform mathematical set operations

In Python, sets are built-in and optimized for performance.

---

## 2. Visual / Example

Given elements:

[1, 2, 2, 3, 4, 4]


Converted into a set:

{1, 2, 3, 4}


Duplicate values are automatically removed.

Set operations example:

A = {1, 2, 3}

B = {3, 4, 5}

Union → {1, 2, 3, 4, 5}

Intersection → {3}

Difference → {1, 2}


---

## 3. Time & Space Complexity

| Operation | Average Case | Worst Case |
|----------|--------------|------------|
| Insert  | O(1)         | O(n)       |
| Search  | O(1)         | O(n)       |
| Delete  | O(1)         | O(n)       |

Space Complexity: **O(n)**

Worst-case performance occurs due to hash collisions.

---

## 4. Python Code

### Basic Set Operations

```python
# Creating a set
numbers = {1, 2, 2, 3, 4}
print(numbers)

# Add element
numbers.add(5)

# Remove element
numbers.remove(2)

# Membership check
print(3 in numbers)
```
### Output

```python
{1, 2, 3, 4}
True

```
### Set Operations Example
```python
A = {1, 2, 3}
B = {3, 4, 5}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)

```
### Output
```python
Union: {1, 2, 3, 4, 5}
Intersection: {3}
Difference: {1, 2}

```
## 5. Common Interview Problems

- Remove duplicates from an array

- Find common elements between lists

- Detect cycles using visited sets

- Longest consecutive sequence

- Unique character checks

These emphasize fast lookup and uniqueness tracking.

---

## 6. ML Connection

Sets play an important role in machine learning workflows:

- Removing duplicate data samples

- Vocabulary building in NLP

- Tracking visited states in graph algorithms

- Feature uniqueness validation

- Dataset cleaning

Efficient set usage improves preprocessing speed.

---

## 7. Practice Tasks

1. Remove duplicates from a list using sets

2. Find intersection of two arrays

3. Detect repeated elements

4. Build a unique word extractor

5. Compare dataset uniqueness

---

**Author:**  
Hamna Munir
