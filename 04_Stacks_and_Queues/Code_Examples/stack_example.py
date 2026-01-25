# Stack Example Implementation

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
print("Popped element:", stack.pop())
print("Top after pop:", stack.peek())

# Output:
# Top element: 30
# Popped element: 30
# Top after pop: 20
