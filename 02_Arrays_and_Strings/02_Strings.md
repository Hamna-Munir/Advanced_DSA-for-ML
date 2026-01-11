# Strings

## 1. Concept Explanation 
A string is a **sequence of characters** used to store and manipulate text data.  
In most programming languages, strings are treated as arrays of characters, allowing indexed access and traversal.

Strings are widely used in data processing, Natural Language Processing (NLP), and feature extraction tasks in Machine Learning.

---

## 2. Visual / Example

Consider the string:

Text: `"model"`

Index:  0   1   2   3   4  
Chars:  m   o   d   e   l  

Each character can be accessed using its index.  
Unlike lists, strings in Python are **immutable**, meaning they cannot be modified in place.

---

## 3. Time & Space Complexity

| Operation                | Time Complexity |
|--------------------------|-----------------|
| Access by index          | O(1)            |
| Traversal                | O(n)            |
| Concatenation            | O(n)            |
| Substring creation       | O(n)            |

**Space Complexity:**  
- O(n), where `n` is the length of the string

Immutability often leads to extra memory usage during string operations.

---

## 4. Python Code

```python
# Creating a string
text = "machine learning"

# Accessing characters
print(text[0])
print(text[8])

# Traversing a string
for char in text:
    print(char)

# String operations
print(text.upper())
print(text.replace("machine", "deep"))
print(len(text))

```
---

## 5. Common Interview Problems

Typical string-related interview problems include:

- Reverse a string

- Check if a string is a palindrome

- Find the first non-repeating character

- Count character frequency

- Longest substring without repeating characters

These problems test logic, edge cases, and optimization skills.

---

## 6. ML Connection

Strings play a crucial role in Machine Learning:

- Text data in NLP is processed as strings

- Tokenization converts strings into numerical representations

- Feature extraction relies on string manipulation

- Labels and categories are often stored as strings

Strong string-handling skills are essential for NLP pipelines and text-based ML systems.

---

## 7. Practice Tasks

1. Reverse a string without using built-in functions

2. Count the number of vowels in a string

3. Check whether a string is a palindrome

4. Remove duplicate characters

5. Find the longest word in a sentence

---

**Author:**  
Hamna Munir
