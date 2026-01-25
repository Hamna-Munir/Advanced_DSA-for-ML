# Stack

## 1. Concept Explanation 
A Stack is a linear data structure that follows the principle:

**LIFO — Last In, First Out**

This means:
- The last element inserted is the first one removed  
- All operations happen from **one end only**, called the *top* of the stack  

Stacks are commonly used to manage:
- Function calls  
- Undo/Redo operations  
- Expression evaluation  
- Backtracking algorithms  

---

## 2. Visual / Example

Push → [ 10 ]

[ 20 ]

[ 30 ] ← Top


Operations:
- **Push** → Add an element on top  
- **Pop**  → Remove the top element  
- **Peek** → View the top element  

---

## 3. Time & Space Complexity

| Operation | Time Complexity |
|-----------|-----------------|
| Push      | O(1)            |
| Pop       | O(1)            |
| Peek      | O(1)            |
| Search    | O(n)            |

**Space Complexity:**  
- O(n) for storing `n` elements  

Stacks are highly efficient because all operations occur at one end.

---

## 4. Python Code

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())
print("Popped:", stack.pop())
print("Top after pop:", stack.peek())
```
### Output
```python
Top element: 30
Popped: 30
Top after pop: 20
```
---

## 5. Common Interview Problems

Frequently asked stack problems include:

- Reverse a string using a stack

- Check balanced parentheses

- Implement stack using queues

- Evaluate postfix expressions

- Find the next greater element

These problems test understanding of LIFO behavior and control flow.

---

## 6. ML Connection

Stacks are used in:

- Backpropagation (function call stack during recursion)

- Expression parsing in model configuration

- Undo/redo operations in ML experiment tracking

- Tree and graph traversals

- Backtracking in optimization algorithms

Understanding stacks helps ML engineers design robust training pipelines and recursive model components.

---

## 7. Practice Tasks

1. Implement stack using a linked list

2. Reverse a list using a stack

3. Check balanced brackets in an expression

4. Implement min-stack (get minimum in O(1))

5. Convert infix expression to postfix

---

**Author:**  
Hamna Munir
