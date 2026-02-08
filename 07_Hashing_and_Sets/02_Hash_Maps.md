# Hash Maps

## 1. Concept Explanation 
A **Hash Map** is a data structure that stores data as **key–value pairs**, allowing extremely fast lookup, insertion, and deletion.

It works by using a **hash function** to convert a key into an index in a hash table. This allows direct access instead of searching through the entire dataset.

Hash maps are widely used for:
- Counting frequencies
- Fast lookups
- Indexing data
- Caching results

In Python, hash maps are implemented using **dictionaries**.

---

## 2. Visual / Example

Key–value pairs to store:

"apple" → 3
"banana" → 5
"orange" → 2

Internal mapping:

hash("apple") → index 4 → value 3
hash("banana") → index 1 → value 5
hash("orange") → index 7 → value 2


Each key maps to a storage location where its value is stored.

---

## 3. Time & Space Complexity

| Operation | Average Case | Worst Case |
|----------|--------------|------------|
| Insert  | O(1)         | O(n)       |
| Search  | O(1)         | O(n)       |
| Delete  | O(1)         | O(n)       |

Space Complexity: **O(n)**

Worst case occurs when collisions degrade performance.

---

## 4. Python Code

### Using Python Dictionary (Hash Map)

```python
# Hash map example
hash_map = {}

# Insert key-value pairs
hash_map["apple"] = 3
hash_map["banana"] = 5
hash_map["orange"] = 2

# Access values
print("Apple count:", hash_map["apple"])

# Update value
hash_map["apple"] += 1

# Iterate through hash map
for key, value in hash_map.items():
    print(key, "->", value)

# Membership check
print("banana" in hash_map)
```
### Output
```python
Apple count: 3
apple -> 4
banana -> 5
orange -> 2
True
```
### Frequency Counting Example
```python

text = "machine learning is powerful"

freq = {}

for word in text.split():
    freq[word] = freq.get(word, 0) + 1

print(freq)
```
### Output
```python
{'machine': 1, 'learning': 1, 'is': 1, 'powerful': 1}

```
## 5. Common Interview Problems

- Two-sum problem

- First non-repeating character

- Frequency counting

- Group anagrams

- Duplicate detection

These problems emphasize efficient lookup and counting.

---

## 6. ML Connection

Hash maps are essential in ML workflows:

- Feature frequency tracking

- Token indexing in NLP

- Caching intermediate computations

- Fast dataset lookup

- Mapping categorical variables

Efficient hash map usage improves data pipeline performance.

---

## 7. Practice Tasks

1. Implement hash map from scratch

2. Count word frequencies in a dataset

3. Solve two-sum using hash map

4. Group words by frequency

5. Build a caching system using hash map

---

**Author:**  
Hamna Munir

