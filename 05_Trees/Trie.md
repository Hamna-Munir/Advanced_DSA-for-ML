# Trie (Prefix Tree)

## 1. Concept Explanation (Simple English)
A **Trie** (also called a **Prefix Tree**) is a special **tree data structure** used to store and efficiently search **strings and prefixes**.

- Each node represents a **character**
- Paths from root to leaf form **words**
- Common prefixes are **shared**, saving memory and time  

Tries are extremely fast for:
- Word search  
- Prefix queries  
- Autocomplete systems  
- Dictionary implementations  

Unlike hash tables, Tries allow **efficient prefix-based searching**.

---

## 2. Visual / Example

Words inserted: `cat`, `car`, `dog`  

```python

      (root)
     /      \
    c        d
    |        |
    a        o
   / \        \
  t   r        g
```

- Each path from root forms a word  
- Nodes are shared for common prefixes (`ca`)  
- End-of-word nodes are specially marked  

Search examples:
- Search "cat" → found  
- Prefix "ca" → matches `cat`, `car`  

---

## 3. Time & Space Complexity

| Operation        | Complexity |
|------------------|------------|
| Insert Word      | O(L)       |
| Search Word      | O(L)       |
| Prefix Search    | O(L)       |
| Space Complexity | O(N × L)   |

Where:
- `L` = length of word  
- `N` = number of words  

Trie operations depend on **word length, not number of words** — very efficient for large dictionaries.

---

## 4. Python Code

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


# Example usage
trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("dog")

print("Search 'cat':", trie.search("cat"))
print("Search 'cap':", trie.search("cap"))
print("Prefix 'ca':", trie.starts_with("ca"))
print("Prefix 'do':", trie.starts_with("do"))
```
### Output
```python
Search 'cat': True
Search 'cap': False
Prefix 'ca': True
Prefix 'do': True
```
---

## 5. Common Interview Problems

- Implement Trie from scratch

- Design autocomplete system

- Word search in dictionary

- Longest common prefix

- Replace words using Trie

- Implement spell checker

These problems test string processing, memory optimization, and tree traversal.

---

## 6. ML Connection

Tries are extremely important in Machine Learning and NLP:

- Autocomplete & Search Engines

- Tokenization in NLP pipelines

- Spell correction systems

- Prefix-based feature indexing

- Vocabulary storage for language models

In NLP systems:

- Fast lookup of tokens

- Efficient prefix matching

- Building dictionaries for embeddings

Many real-world ML systems rely on Tries internally.

---


## 7. Practice Tasks

1. Implement Trie with delete operation

2. Build an autocomplete system using Trie

3. Find all words with a given prefix

4. Count number of words with prefix

5. Implement longest common prefix using Trie

---

**Author:**  
Hamna Munir
