# Longest Common Subsequence

## 1. Concept Explanation
The **Longest Common Subsequence (LCS)** problem is a classic problem in **Dynamic Programming**.

A **subsequence** is a sequence that appears in the same relative order but **not necessarily contiguous**.

The goal of LCS is to find the **longest sequence of characters that appear in both strings in the same order**.

Example:

String 1: `ABCBDAB`  
String 2: `BDCAB`

One possible common subsequence is:

`BCAB`

Length = **4**

Dynamic Programming is used because the problem contains:

- **Overlapping subproblems**
- **Optimal substructure**

Instead of recomputing subproblems, we store results in a **DP table**.

---

## 2. Visual / Example

Example strings:

Text1 = "ABC"

Text2 = "AC"

### Possible subsequences of `"ABC"`:

A

B

C

AB

AC

BC

ABC

### Common subsequences with `"AC"`:

A

C

AC

### The **Longest Common Subsequence** is:

AC

Length = **2**

### Dynamic Programming builds a table comparing characters from both strings.

Example DP table structure:

  A  C

  0 0 0
  
A 0 1 1

B 0 1 1

C 0 1 2


Final result is the value in the **bottom-right cell**.

---

## 3. Time & Space Complexity

For strings of length **m** and **n**:

- Time Complexity: **O(m × n)**
- Space Complexity: **O(m × n)**

Optimized solutions can reduce space complexity to **O(min(m, n))**.

---

## 4. Python Code

### Longest Common Subsequence Using Dynamic Programming

```python
def lcs(text1, text2):

    m = len(text1)
    n = len(text2)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]


text1 = "ABCBDAB"
text2 = "BDCAB"

print(lcs(text1, text2))
```
### Output
```python
4
```
---

## 5. Common Interview Problems

- Longest Common Subsequence

- Longest Common Substring

- Edit Distance

- Minimum Insertions to Form Palindrome

- Shortest Common Supersequence

These problems test understanding of string dynamic programming techniques.

---

## 6. ML Connection

LCS concepts appear in many machine learning and AI applications:

- Text similarity analysis

- Natural Language Processing (NLP)

- DNA sequence alignment in bioinformatics

- Version control systems (diff algorithms)

- Document comparison systems

Understanding LCS helps in solving problems related to sequence matching and similarity detection.

---

## 7. Practice Tasks

1. Modify the program to print the actual LCS string

2. Solve Longest Common Substring

3. Implement Edit Distance

4. Compare recursive vs DP solutions

5. Trace the DP table manually for small strings

These exercises strengthen understanding of dynamic programming for strings.

---

**Author:**  
Hamna Munir
